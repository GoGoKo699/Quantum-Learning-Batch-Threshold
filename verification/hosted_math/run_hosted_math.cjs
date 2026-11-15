'use strict';
// Local runtime adapter. The three canonical inspection helpers stay unchanged.
// Reset only ordinary scroll state and wait for GitHub's sticky header to settle.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const collector = require('./capture_hosted_math.cjs');
const probe = require('./probe_hosted_math.cjs');

async function settleScroll(page, y) {
  await page.evaluate(target => new Promise(resolve => {
    window.scrollTo(0, target);
    requestAnimationFrame(() => requestAnimationFrame(resolve));
  }), y);
  await page.waitForTimeout(200);
}

function fileRecord(filename) {
  const bytes = fs.readFileSync(filename);
  return {path:path.basename(filename),size_bytes:bytes.length,
    sha256:crypto.createHash('sha256').update(bytes).digest('hex')};
}

async function loadRuntime(args) {
  const {chromium} = require('playwright');
  const browser = await chromium.launch({headless:true});
  const adapterHash = crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
  const supplementManifest = {schema_version:1,kind:'actual_browser_visual_supplements',
    repository:args.repository,revision:args.revision,tree:collector.pinnedPages(args).tree,
    runtime_adapter_sha256:adapterHash,
    limits:'Additional ordinary-scroll viewport screenshots; separate from canonical structural-comparison artifacts.',captures:[]};
  const newContext = browser.newContext.bind(browser);
  browser.newContext = async options => {
    const context = await newContext(options);
    const newPage = context.newPage.bind(context);
    context.newPage = async () => {
      const page = await newPage();
      const screenshot = page.screenshot.bind(page);
      page.screenshot = async (options = {}) => {
        await settleScroll(page, 0);
        await page.waitForFunction(() => window.scrollY === 0, null, {timeout:5000});
        const result = await screenshot(options);
        if (typeof options.path !== 'string' || !options.fullPage) return result;
        const stem = options.path.replace(/\.png$/i, '');
        const row = {url:page.url(),viewport:page.viewportSize(),
          canonical_screenshot:fileRecord(options.path),supplements:[]};
        try {
          for (const [label, y] of [['top',0],['500',500]]) {
            await settleScroll(page, y);
            const filename = stem+'-supplement-'+label+'.png';
            await screenshot({...options,path:filename,fullPage:false});
            row.supplements.push({...fileRecord(filename),requested_scroll_y:y,
              actual_scroll_y:await page.evaluate(() => window.scrollY),observed_at:new Date().toISOString()});
          }
        } finally {
          await settleScroll(page, 0);
        }
        supplementManifest.captures.push(row);
        fs.writeFileSync(path.join(args.output,'visual-supplements.json'),JSON.stringify(supplementManifest,null,2)+'\n');
        return result;
      };
      return page;
    };
    return context;
  };
  return {
    browser,
    compile:collector.mathCompiler(),
    runtime:{
      node:process.version,
      playwright:require('playwright/package.json').version,
      mathjax:require('mathjax-full/package.json').version,
      browser:browser.version(),
      runtime_adapter_sha256:adapterHash,
      screenshot_scroll_reset:'ordinary scroll, two animation frames, 200ms settling; supplementary viewport captures at top and scrollY500; no content/style mutation'
    }
  };
}

(async () => {
  const [mode, ...argv] = process.argv.slice(2);
  if (!['probe','capture'].includes(mode)) throw new Error('Use probe or capture followed by the canonical arguments');
  const args = mode === 'probe' ? probe.argumentsFor(argv) : collector.argumentsFor(argv);
  if (args.help) {
    console.log('run_hosted_math.cjs probe|capture --root REPO --repository owner/name --revision FULLSHA --output EMPTY_DIR [--page PATH]');
    return;
  }
  if (mode === 'probe') {
    const result = await probe.run(args, {capture:a => collector.run(a, {loadRuntime:() => loadRuntime(a)})});
    console.log(JSON.stringify({status:result.report.status,category:result.report.failure_category,
      report:path.join(path.resolve(args.output),'probe-report.json'),release_ready:false}));
    process.exitCode = result.code;
  } else {
    process.exitCode = await collector.run(args, {loadRuntime:() => loadRuntime(args)});
  }
})().catch(error => {console.error(String(error)); process.exitCode = 2;});

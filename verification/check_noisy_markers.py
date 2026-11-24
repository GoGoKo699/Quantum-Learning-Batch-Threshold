#!/usr/bin/env python3
"""Finite diagnostics for marker exclusion and the attaining GHZ measurement."""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction

import numpy as np


TOL = 3e-11
SEED = 20261124
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)


def require(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def rational_laws(integer_rows, denominator):
    return tuple(tuple(Fraction(entry, denominator) for entry in row)
                 for row in integer_rows)


def product_laws(laws, size):
    outcomes = itertools.product(range(len(laws[0])), repeat=size)
    outcomes = tuple(outcomes)
    return tuple(tuple(math.prod(row[outcome] for outcome in word)
                       for word in outcomes) for row in laws)


def cross_product(left, right):
    return tuple(left[(i + 1) % 3] * right[(i + 2) % 3]
                 - left[(i + 2) % 3] * right[(i + 1) % 3] for i in range(3))


def bayesian_exclusion(laws, prior):
    return sum(min(weight * probability for weight, probability in zip(prior, column))
               for column in zip(*laws))


def exact_dual_exclusion(laws):
    """Maximize the piecewise-linear Bayes risk at simplex subdivision vertices."""
    planes = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
    for column in zip(*laws):
        for left, right in itertools.combinations(range(3), 2):
            plane = [0, 0, 0]
            plane[left], plane[right] = column[left], -column[right]
            if any(plane):
                planes.add(tuple(plane))
    best = Fraction(0)
    for left, right in itertools.combinations(planes, 2):
        direction = cross_product(left, right)
        total = sum(direction)
        if total != 0 and all(component * total >= 0 for component in direction):
            prior = tuple(Fraction(component, total) for component in direction)
            best = max(best, bayesian_exclusion(laws, prior))
    return best


def omission_laws(laws, rule):
    """The axis-conditional probabilities of each of the three omissions."""
    for column in zip(*rule):
        require(sum(column) == 1 and min(column) >= 0, "Invalid omission rule")
    return tuple(tuple(sum(p * r for p, r in zip(row, decision)) for decision in rule)
                 for row in laws)


def goldar_laws(size, strength):
    return tuple(tuple(math.comb(size, count) * bias**count
                       * (1 - bias)**(size - count) for count in range(size + 1))
                 for bias in ((1 - strength) / 2, Fraction(1, 2), (1 + strength) / 2))


def goldar_symmetric_dual(laws):
    """Evaluate every breakpoint of the reflection-symmetric Bayes risk."""
    extreme_min = tuple(map(min, zip(laws[0], laws[2])))
    middle = laws[1]
    weights = (Fraction(0), Fraction(1)) + tuple(
        p / (2 * q + p) for p, q in zip(extreme_min, middle))
    return max(sum(min(weight * q, (1 - weight) * p / 2)
                   for p, q in zip(extreme_min, middle)) for weight in weights)


def check_finite_exclusion():
    erasure = rational_laws(((1, 0, 0, 2), (0, 1, 0, 2), (0, 0, 1, 2)), 3)
    for size in (1, 2, 3):
        actual = exact_dual_exclusion(product_laws(erasure, size))
        require(actual == Fraction(2, 3)**size / 3, "Erasure benchmark differs")

    no_common_symbol = rational_laws(((1, 1, 0), (1, 0, 1), (0, 1, 1)), 2)
    require(exact_dual_exclusion(no_common_symbol) == 0, "Expected perfect exclusion")
    require(sum(map(max, zip(*no_common_symbol))) < 3,
            "Expected positive identification error with perfect exclusion")

    asymmetric = rational_laws(((7, 2, 1), (2, 5, 3), (1, 3, 6)), 10)
    rule = rational_laws(((0, 12, 31), (0, 11, 0), (31, 8, 0)), 31)
    omitted = omission_laws(asymmetric, rule)
    prior = tuple(Fraction(weight, 31) for weight in (15, 6, 10))
    value = Fraction(11, 62)
    require(max(omitted[axis][axis] for axis in range(3)) == value,
            "Asymmetric primal certificate differs")
    require(bayesian_exclusion(asymmetric, prior) == value,
            "Asymmetric dual certificate differs")
    require(exact_dual_exclusion(asymmetric) == value, "Asymmetric minimax value differs")
    return {"cases": 5, "asymmetric_value": str(value)}, omitted


def check_goldar():
    cases = 0
    for strength in map(Fraction, ("0.08", "0.25", "0.49")):
        for size in (1, 2, 3, 4, 8, 16, 32, 64):
            laws = goldar_laws(size, strength)
            value = goldar_symmetric_dual(laws)
            binary = sum(map(min, zip(laws[0], laws[2]))) / 2
            ratio = max(min(x, z) / y for x, y, z in zip(*laws))
            require(2 * binary / (2 + ratio) <= value <= binary,
                    "Goldar binary-overlap bounds differ")
            if size <= 4:
                require(value == exact_dual_exclusion(laws),
                        "Symmetric and full-prior optimizations differ")
            if size == 1:
                require(value == (1 - strength) / (3 - strength),
                        "Single-copy exclusion formula differs")
            cases += 1
    return {"cases": cases, "batch_sizes_through": 64}


def word_matrix(word, multiplicity=1):
    matrix = np.ones((1, 1), dtype=complex)
    for axis in word:
        for _ in range(multiplicity):
            matrix = np.kron(matrix, PAULI[axis])
    return matrix


def check_weighted_pauli():
    rng = np.random.default_rng(SEED)
    cases = 0
    for sites, multiplicity in ((1, 1), (2, 1), (3, 1), (4, 1), (1, 3), (2, 3)):
        words = tuple(itertools.product(range(3), repeat=sites))
        matrices = tuple(word_matrix(word, multiplicity) for word in words)
        dimension = 2 ** (sites * multiplicity)
        for _ in range(24):
            posteriors = rng.dirichlet([1, 1, 1], size=sites)
            state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
            state /= np.linalg.norm(state)
            weighted = sum(math.prod(posteriors[i, axis] for i, axis in enumerate(word))
                           * abs(np.vdot(state, matrix @ state))**2
                           for word, matrix in zip(words, matrices))
            require(weighted <= np.prod(1 - posteriors.min(axis=1)) + TOL,
                    "Posterior-weighted odd Pauli budget violated")
            cases += 1
    return {"cases": cases, "seed": SEED}


def ghz_basis(sites, parity):
    dimension = 2**sites
    basis = np.zeros((dimension, dimension), dtype=complex)
    for representative in range(dimension // 2):
        complement = dimension - 1 - representative
        basis[representative, 2 * representative:2 * representative + 2] = 1
        basis[complement, 2 * representative:2 * representative + 2] = (1, -1)
    if parity == 1:
        basis[dimension // 2:] *= 1j
    return basis / math.sqrt(2)


def check_ghz_sign_and_coverage(omitted):
    cases = 0
    for sites in range(1, 5):
        dimension = 2**sites
        identity = np.eye(dimension)
        bases = [ghz_basis(sites, parity) for parity in (0, 1)]
        for word in itertools.product((0, 1), repeat=sites):
            matrix = word_matrix(word)
            parity = sum(word) % 2
            basis = bases[parity]
            in_basis = basis.conj().T @ matrix @ basis
            sign = np.diag(in_basis).real
            require(np.allclose(in_basis, np.diag(sign), rtol=0, atol=TOL),
                    "A retained parity word is not diagonal in its GHZ basis")
            require(np.allclose(np.abs(sign), 1, rtol=0, atol=TOL),
                    "A retained parity word has a nonbinary decoded eigenvalue")
            for contrast in (-1, -0.37, 0, 0.63, 1):
                state = (identity + contrast * matrix) / dimension
                born = np.diag(basis.conj().T @ state @ basis).real
                require(abs(born @ sign - contrast) <= TOL, "Decoded sign has wrong mean")
            cases += 1

        words = tuple(itertools.product(range(3), repeat=sites))
        for word in words:
            eligibility = Fraction(0)
            for omissions in words:
                probability = math.prod(omitted[axis][omit]
                                        for axis, omit in zip(word, omissions))
                if any(axis == omit for axis, omit in zip(word, omissions)):
                    continue
                retained = [[candidate for candidate in range(3) if candidate != omit]
                            for omit in omissions]
                matches = sum(options.index(axis) for axis, options in zip(word, retained)) % 2
                eligibility += sum(probability / 2 for parity in (0, 1) if parity == matches)
            expected = math.prod(1 - omitted[axis][axis] for axis in word) / 2
            require(eligibility == expected, "Coverage differs from the product formula")
            cases += 1
    return {"cases": cases, "sites_through": 4}


def check_all():
    finite, omitted = check_finite_exclusion()
    groups = {
        "exact_finite_exclusion": finite,
        "exact_goldar_binomial": check_goldar(),
        "weighted_odd_pauli_budget": check_weighted_pauli(),
        "ghz_sign_and_exact_marker_coverage": check_ghz_sign_and_coverage(omitted),
    }
    return {"cases": sum(group["cases"] for group in groups.values()), "groups": groups}


def main():
    print(json.dumps({"passed": True, **check_all()}, sort_keys=True))


if __name__ == "__main__":
    main()

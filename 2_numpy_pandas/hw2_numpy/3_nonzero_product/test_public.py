import numpy as np
from numpy.testing import assert_array_equal

import pytest
import typing as tp
import dataclasses

from .nonzero_product import nonzero_product


@dataclasses.dataclass
class NonzeroProductCase:
    matrix: tp.Any
    result: tp.Any


NONZERO_PRODUCT_TEST_CASES = [
    NonzeroProductCase(
        matrix=np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]),
        result=3),
    NonzeroProductCase(
        matrix=np.array([[0, 0, 1], [2, 0, 2], [3, 0, 0], [4, 4, 4]]),
        result=None),
    NonzeroProductCase(
        matrix=np.array([[], [], [], []]),
        result=None),
    NonzeroProductCase(
        matrix=np.arange(24).reshape((4, 6)),
        result=2058),
    NonzeroProductCase(
        matrix=np.ones(48).reshape((12, 4)),
        result=1),
    NonzeroProductCase(
        matrix=np.zeros(48).reshape((12, 4)),
        result=None),
    NonzeroProductCase(
        matrix=np.array([[1]]),
        result=1),
    NonzeroProductCase(
        matrix=np.array([[0]]),
        result=None),
    NonzeroProductCase(
        matrix=np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        result=1),
]


@pytest.mark.parametrize('t', NONZERO_PRODUCT_TEST_CASES, ids=str)
def test_construct_matrix(t: NonzeroProductCase) -> None:
    assert_array_equal(nonzero_product(t.matrix), t.result)

import numpy as np
from numpy.testing import assert_array_equal

import pytest
import typing as tp
import dataclasses

from .vander import vander


@dataclasses.dataclass
class VanderCase:
    array: tp.Any
    result: tp.Any


VANDER_TEST_CASES = [
    VanderCase(
        array=np.array([1]),
        result=np.array([[1]])),
    VanderCase(
        array=np.array([1, 2, 3]),
        result=np.array([[1, 1, 1], [1, 2, 4], [1, 3, 9]])),
    VanderCase(
        array=np.ones(3),
        result=np.ones((3, 3)))
]


@pytest.mark.parametrize('t', VANDER_TEST_CASES, ids=str)
def test_construct_matrix(t: VanderCase) -> None:
    assert_array_equal(vander(t.array), t.result)


def test_random_matrix() -> None:
    np.random.seed(42)

    for _ in range(100):
        matrix = np.random.randint(1, 10, 10)
        assert_array_equal(vander(matrix), np.vander(matrix, increasing=True))

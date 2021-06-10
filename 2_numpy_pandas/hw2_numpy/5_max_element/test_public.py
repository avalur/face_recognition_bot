import numpy as np
from numpy.testing import assert_array_equal

import pytest
import typing as tp
import dataclasses

from .max_element import max_element


@dataclasses.dataclass
class MaxElementCase:
    array: tp.Any
    result: tp.Any


MAX_ELEMENT_TEST_CASES = [
    MaxElementCase(
        array=np.array([1, 0, 2, 3]),
        result=2),
    MaxElementCase(
        array=np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]),
        result=5),
    MaxElementCase(
        array=np.array([6, 6]),
        result=None),
    MaxElementCase(
        array=np.zeros(3),
        result=0),
    MaxElementCase(
        array=np.array([0, 1]),
        result=1),
    MaxElementCase(
        array=np.array([1, 0]),
        result=None),
    MaxElementCase(
        array=np.array([1, 0, 0, -1]),
        result=0),
    MaxElementCase(
        array=np.array([0]),
        result=None),
    MaxElementCase(
        array=np.array([1]),
        result=None),
    MaxElementCase(
        array=np.array([0, 1, 2, 0, 10]),
        result=10),
    MaxElementCase(
        array=np.array([6, 2, 0, 3, 0, 0, 9, 4]),
        result=9),
]


@pytest.mark.parametrize('t', MAX_ELEMENT_TEST_CASES, ids=str)
def test_construct_matrix(t: MaxElementCase) -> None:
    assert_array_equal(max_element(t.array), t.result)

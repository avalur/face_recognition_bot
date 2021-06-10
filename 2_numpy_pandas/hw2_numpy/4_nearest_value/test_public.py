import numpy as np

import pytest
import typing as tp
import dataclasses

from .nearest_value import nearest_value


@dataclasses.dataclass
class NearestValueCase:
    matrix: tp.Any
    value: float
    result: tp.Any


NEAREST_VALUE_TEST_CASES = [
    NearestValueCase(
        matrix=np.arange(0, 10).reshape((2, 5)),
        value=3.6,
        result=4.),
    NearestValueCase(
        matrix=np.arange(0, 10).reshape((5, 2)),
        value=0.3,
        result=0.0),
    NearestValueCase(
        matrix=np.arange(0, 10).reshape((10, 1)),
        value=0.6,
        result=1.0),
    NearestValueCase(
        matrix=np.zeros((5, 10)),
        value=20.0,
        result=0.0),
    NearestValueCase(
        matrix=np.array([[1, 0, 0]]),
        value=0.9,
        result=1.0),
    NearestValueCase(
        matrix=np.array([[0, 0, 1]]),
        value=0.9,
        result=1.0),
    NearestValueCase(
        matrix=np.array([[1]]),
        value=1000000,
        result=1.0),
]


@pytest.mark.parametrize('t', NEAREST_VALUE_TEST_CASES, ids=str)
def test_construct_matrix(t: NearestValueCase) -> None:
    assert np.isclose(nearest_value(t.matrix, t.value), t.result)


def test_random_matrix() -> None:
    np.random.seed(42)
    for _ in range(100):
        shape = np.random.randint(2, 100, size=2)
        matrix = np.random.rand(*shape)
        for value in np.random.choice(np.ravel(matrix), 10):
            assert np.isclose(nearest_value(matrix, value), value)

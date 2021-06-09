import copy
import dataclasses
import typing as tp

import pytest


from .bin_basic import find_value


@dataclasses.dataclass
class Case:
    nums: tp.Sequence[int]
    value: int
    result: bool
    name: tp.Optional[str] = None

    def __str__(self) -> str:
        if self.name is not None:
            return self.name
        return 'find_{}_in_{}'.format(self.value, self.nums)


BIG_VALUE = 10**15

TEST_CASES = [
    Case(nums=[], value=2, result=False),
    Case(nums=[1], value=2, result=False),
    Case(nums=[1, 3, 5], value=0, result=False),
    Case(nums=[1, 3, 5], value=2, result=False),
    Case(nums=[1, 3, 5], value=4, result=False),
    Case(nums=[1, 3, 5], value=6, result=False),
    Case(nums=[1, 3, 5], value=1, result=True),
    Case(nums=[1, 3, 5], value=3, result=True),
    Case(nums=[1, 3, 5], value=5, result=True),
    Case(nums=[3], value=3, result=True),
    Case(nums=[1, 3], value=1, result=True),
    Case(nums=[1, 3], value=3, result=True),
    Case(nums=[1, 3, 5, 7], value=0, result=False),
    Case(nums=[1, 3, 5, 7], value=2, result=False),
    Case(nums=[1, 3, 5, 7], value=4, result=False),
    Case(nums=[1, 3, 5, 7], value=6, result=False),
    Case(nums=[1, 3, 5, 7], value=8, result=False),
    Case(nums=[1, 3, 5, 7], value=1, result=True),
    Case(nums=[1, 3, 5, 7], value=3, result=True),
    Case(nums=[1, 3, 5, 7], value=5, result=True),
    Case(nums=[1, 3, 5, 7], value=7, result=True),
    Case(nums=[1, 3, 5, 7, 9], value=0, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=2, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=4, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=6, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=8, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=10, result=False),
    Case(nums=[1, 3, 5, 7, 9], value=1, result=True),
    Case(nums=[1, 3, 5, 7, 9], value=3, result=True),
    Case(nums=[1, 3, 5, 7, 9], value=5, result=True),
    Case(nums=[1, 3, 5, 7, 9], value=7, result=True),
    Case(nums=[1, 3, 5, 7, 9], value=9, result=True),
    Case(nums=[1, 5, 5, 5, 9], value=1, result=True),
    Case(nums=[1, 5, 5, 5, 9], value=5, result=True),
    Case(nums=[1, 5, 5, 5, 9], value=9, result=True),
    Case(nums=[1, 5, 5, 5, 9], value=7, result=False),
    Case(nums=range(0, BIG_VALUE, 2), value=BIG_VALUE - 2,
         result=True, name="max_in_big_range"),
    Case(nums=range(0, BIG_VALUE, 2), value=0,
         result=True, name="min_in_big_range"),
    Case(nums=range(0, BIG_VALUE, 2), value=BIG_VALUE,
         result=False, name="greater_than_max_in_big_range"),
    Case(nums=range(0, BIG_VALUE, 2), value=-1,
         result=False, name="less_than_min_in_big_range"),
    Case(nums=range(0, BIG_VALUE, 2), value=BIG_VALUE // 2,
         result=True, name="middle_in_big_range"),
    Case(nums=range(0, BIG_VALUE, 2), value=BIG_VALUE // 2 + 1,
         result=False, name="middle_not_exists_in_big_range"),
]


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_find_value(t: Case) -> None:
    nums_copy = copy.deepcopy(t.nums)

    answer = find_value(nums_copy, t.value)

    assert t.nums == nums_copy, "You shouldn't change inputs"
    assert answer == t.result

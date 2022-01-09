# python의 배열구조는 동적 배열 자료형므로 리스트에 아이템을 추가할때 마다 용량이 꽉 차게 되면 (max data=4 에서 하나더 추가) 동적으로 용량을 늘린다.


# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자의 인덱스를 리턴
nums = [2, 7, 11, 15]
target = 9

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, i_num in enumerate(nums):
        if target - i_num in nums_map:
            return [i, nums_map[target - i_num]]

        nums_map[i_num] = i


print(twoSum(nums, target))
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = collections.defaultdict(int)

        for num in nums:
            if dict[num] == 0:
                dict[num] = nums.count(num)

            if dict[num] > len(nums)//2:
                return num


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if nums is None:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b,a][nums.count(a) > half]
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))
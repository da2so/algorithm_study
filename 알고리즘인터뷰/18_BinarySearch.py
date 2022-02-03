from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
nums = [-1, 0, 3, 5, 9, 12]
target = 9

nums = [-1,0,3,5,9,12]
target = -2
sol = Solution()
print(sol.search(nums, target))



from bisect import bisect_left, bisect_right

nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 4
print(bisect_left(nums, n))
print(bisect_right(nums, n))

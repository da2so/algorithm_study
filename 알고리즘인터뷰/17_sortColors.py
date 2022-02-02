"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0 , 0, len(nums) -1

        while white <= blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:

                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1

        return nums
nums = [2,0,2,1,1,0]
#nums = [2,0,1]
sol = Solution()
print(sol.sortColors(nums))
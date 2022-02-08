from typing import List

#3개의 원소로 합을 햇을때 0 이되는 조합을 return하라


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i+1]: #같은 원소가 있으면 넘어가자
            continue

        left, right = i+1, len(nums)-1

        while left < right:

            sum = nums[left] + nums[right] + nums[i]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
        return result

nums = [-1, 0, 1, 2, -1 ,4]
print(threeSum(nums))
from typing import List

# 주의사항: 나눗셈을 하지 않고 O(N)에 풀이하라
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []

    p = 1
    #왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]
    return out

nums = [1, 2, 3, 4]

print(productExceptSelf(nums))
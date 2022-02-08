from typing import List
# 배열을 입력받아 ouput[i]가 자신을 제외한 나머지 모든 요소의 곱셈결과가 되도록하라
# 주의사항: 나눗셈을 하지 않고 O(N)에 풀이하라
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []

    p = 1
    #왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p *= nums[i]
    p = 1
    print(out)
    # 오른쪽 곱셈
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]
    return out

nums = [1, 2, 3, 4]

print(productExceptSelf(nums))
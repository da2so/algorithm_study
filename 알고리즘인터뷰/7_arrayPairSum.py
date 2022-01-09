#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

from typing import List
def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

nums = [1, 4, 3, 2]
print(arrayPairSum((nums)))
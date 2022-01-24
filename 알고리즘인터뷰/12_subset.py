
#모든 부분집합을 리턴하라
from typing import List
def subset(nums: List[int]) -> List[List[int]]:
    sorted(nums)
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]])
    dfs(0, [])
    return result

nums = [1,2,3]

print(subset(nums))
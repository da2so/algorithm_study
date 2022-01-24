
from typing import List
def combinationSum(candidates: List[int], target: int)-> List[List[int]]:

    def dfs(remain, index, elements):
        if remain < 0:
            return
        if remain == 0:
            result.append(elements)

        for i in range(index, len(candidates)):
            dfs(remain-candidates[i], i, elements+[candidates[i]] )
    result = []
    dfs(target,0, [])
    return result
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))
import itertools
from typing import List
def combine(n:int , k:int) -> List[List[int]]:

    def dfs(elements, start, k):

        if k == 0:
            result.append(elements[:])
            return

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)

            elements.pop()

    result = []
    dfs([], 1, k)
    return result

def combine_itertools(n:int, k:int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n+1), k ))
n = 4
k = 2
print(combine(n,k))
print(combine_itertools(n,k))
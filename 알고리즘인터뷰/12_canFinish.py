# 0을 완료하기위해서는 1로 끝내야한다는 것을 [0,1] 쌍을 표현하는 n개의 코스가 있다. 코스개수가 n과 이 쌍들을 입력으로 받았을때 모든 코스가 완료가능한지 판별하라.
import collections
from typing import List
def canFinish(a: int, b:List[List[int]])-> bool:

    graph = collections.defaultdict(list)
    for x,y in b:
        graph[x].append(y)
    traced = set()
    visited = set()
    def dfs(i):
        if i in traced:
            return False
        if i in visited: #가지치기
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True

a = 2
b = [[1,0], [0,1]]
b2 = [[0,1], [1,2]]
print(canFinish(a,b2))
import collections
import heapq
from typing import List
def findCheapestPrice(n:int, edge:List[List[int]], src:int, dst:int, K:int) -> int:
    graph = collections.defaultdict(list)

    for u,v,w in edge:
        graph[u].append((v,w))

    Q = [[0,src, K]]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1


n =3
edge =[[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K= 0
print(findCheapestPrice(n,edge,src,dst,K))
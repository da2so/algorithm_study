#K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가하면 -1 을 리턴 ,입력값은 (u, v, w)는 각각 출발지, 도착지 , 소용시간으로 구성되며
# 전체 노드의 개수는 N으로 입력받는다.
import collections
import heapq
from typing import List
def networkDelayTime(times: List[List[int]], N:int, K: int) -> int:
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v,w))

    Q = [[0,K]]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time

            for x, y in graph[node]:
                alt = time + y
                heapq.heappush(Q, (alt, x))

    if N == len(dist):
        return max(dist.values())
    return -1
times = [[2,1,1], [2,3,1], [3,4,1]]
N = 4
K = 2
print(networkDelayTime(times,N,K))
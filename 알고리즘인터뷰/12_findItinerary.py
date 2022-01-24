#[from, to]로 구성된 항공권 목록을 이용행 JFK에서 출발하는 여행 일정을 구성하라. 여러 구성이 있는 경우 사전 어휘순으로 방문한다.
from typing import List
from collections import defaultdict
def findItinerary(s: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    #print(sorted(s))
    for a, b in sorted(s):
        graph[a].append(b)
    print(graph)
    result = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0)) #pop(0) -> O(N)
        result.append(a)
    dfs("JFK")
    return result[::-1]

def findItinerary_efficient(s: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    #print(sorted(s))
    for a, b in sorted(s, reverse=True):
        graph[a].append(b)
    print(graph)
    result = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop()) #pop() -> O(1)
        result.append(a)
    dfs("JFK")
    return result[::-1]


s = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
s2 = [["JFK", "SFO"], ["JFK","ATL"],["SFO","ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(s2))
print(findItinerary_efficient(s2))
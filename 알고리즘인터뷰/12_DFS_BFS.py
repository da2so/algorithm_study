

# 재귀를 이용한 DFS

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

def stack_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        tmp = stack.pop()

        if tmp not in discovered:
            discovered.append(tmp)
            for i in graph[tmp]:
                stack.append(i)

    return discovered

def queue_bfs(start_v):
    discovered = []
    queue = [start_v]

    while queue:
        tmp = queue.pop(0)
        if tmp not in discovered:
            discovered.append(tmp)
            for i in graph[tmp]:
                queue.append(i)

    return discovered



graph = {1: [2, 3, 4],
         2: [5],
         3: [5],
         4: [],
         5: [6, 7],
         6: [],
         7: [3],
         }

print(recursive_dfs(1))
print(stack_dfs(1))
print(queue_bfs((1)))


#back tracking은 탐색을 하다가 더 갈 수 없으면 왓던 길을 돌아가 다른길을 찾는데에서 유래됨
#back tracking은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며, 주로 재귀로 구현된다.
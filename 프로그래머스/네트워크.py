


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i_com in range(n):
        if visited[i_com] == False:
            DFS(i_com, n, computers, visited)
            answer +=1
    return answer

def DFS(i_com, n, computers, visited):
    visited[i_com] = True

    for j_com in range(n):
        if j_com != i_com and computers[i_com][j_com] == 1:
            if visited[j_com] == False:
                DFS(j_com, n, computers, visited)


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

#computers= [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
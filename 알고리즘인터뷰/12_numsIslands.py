
# 1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을 때 섬의 개수를 구하라
from typing import List

def numsIsland(grid: List[List[str]]) -> int:
    result = 0

    def dfs(i, j):
        if i <0 or i>= len(grid) or \
            j <0 or j>= len(grid[0]) or \
            grid[i][j] != '1' :
                return

        grid[i][j] = 0

        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                result += 1

    return result



a = [
      ['1','1','1','1', '0'],
      ['1','1','0','1', '0'],
      ['1','1','0','0', '0'],
      ['0','0','0','0', '0'],
     ]
b = [
      ['1','1','0','0', '0'],
      ['1','1','0','0', '0'],
      ['0','0','1','0', '0'],
      ['0','0','0','1', '1'],
     ]
print(numsIsland(a))
print(numsIsland(b))

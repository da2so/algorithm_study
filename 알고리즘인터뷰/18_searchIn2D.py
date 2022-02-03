"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

"""


class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)


matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
target = 19

sol = Solution()
print(sol.searchMatrix(matrix,target))
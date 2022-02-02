from typing import List
class Solution:

    def distance(self, point):
        return point[0]**2 + point[1]**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        result = []
        for i, point in enumerate(points):
            dist.append([i, self.distance(point)])

        dist.sort(key= lambda x: x[1])

        for j in range(k):
            index = dist[j][0]
            result.append(points[index])
        return result

points = [[3,3],[5,-1],[-2,4]]
k = 2

sol = Solution()
print(sol.kClosest(points,k))
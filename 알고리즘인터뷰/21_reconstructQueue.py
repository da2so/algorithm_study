"""
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people
in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people.
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes
 of the jth person in the queue (queue[0] is the person at the front of the queue).

"""
import heapq
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result= []
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sol = Solution()
print(sol.reconstructQueue(people))
"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
 Tasks could be done in any order. Each task is done in one unit of time.
 For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.


"""

from typing import List
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break
            result += n - sub_count + 1 #idle처리 (most common 수 3일때 가 주어진 알파겟 수는 2개(A,B)임 이럴때 idle추가)
        return result

tasks = ["A","A","A","B","B","B"]
n = 2

sol = Solution()
print(sol.leastInterval(tasks,n))
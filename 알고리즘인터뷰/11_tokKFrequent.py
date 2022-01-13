#상위 k 번 이상 등장하는 요소를 추출하라
import collections
import heapq
from typing import List
def tokKFrequent(nums: List, k: int) -> List:

    freqs = []
    counter = collections.Counter(nums)

    for i in range(len(counter)):
        heapq.heappush(freqs,(-counter[i], i))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs)[1])
    return topk
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(tokKFrequent(nums, k))
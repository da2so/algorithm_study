import itertools
from typing import List
def permute(nums: List[int]) -> List[List[int]]:

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:] #[:]을 통해 값전달
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            print(prev_elements.pop())

    result = []
    prev_elements = []
    dfs(nums)

    return result


def permute_itertools(nums: List[int]) -> List[List[int]]:

    return list(itertools.permutations(nums))


a = [1,2,3]
print(permute(a))
print(permute_itertools(a))
from typing import List
import collections


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams(input))

# more about sort

a = ['cde', 'cfc', 'abc']

def fn(s):
    return s[0], s[-1]
print(sorted(a, key=fn))

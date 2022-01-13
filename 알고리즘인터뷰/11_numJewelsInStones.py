import collections


def numJewelsInStones(J: str, S:str) -> int:

    count = collections.Counter(S)
    result = 0
    for j in J:
        result += count[j]

    return result
J = 'aA'
S = 'aAAbbbb'

print(numJewelsInStones(J,S))
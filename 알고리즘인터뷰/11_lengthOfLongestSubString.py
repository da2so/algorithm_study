


def lengthOfLongestSubString(s: str) -> int:
    set = {}
    start = 0
    result = 0
    for idx, char in enumerate(s):

        if char in set and start <= set[char]:
            start = set[char] + 1
        else:
            result = max(result, idx - start +1)

        set[char] = idx

    return result

s = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'

print(lengthOfLongestSubString(s2))
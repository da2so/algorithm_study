
import collections
#use deque (fast)

def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) >1:
        if strs.popleft() != strs.pop():
            return False

    return True


# slicinng (more faseter)
import re
def isPalindrome(s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]','',s)
    print(s)
    print(type(s))

    return s == s[::-1]
a = 'A man, a plan, a canal: Panama'

print(isPalindrome(a))

#중복된 문자를 제외하고 사전식 순서로 나열하라
import collections


def removeDuplicateLetters(s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)

s = 'bcabc'

print(removeDuplicateLetters(s))
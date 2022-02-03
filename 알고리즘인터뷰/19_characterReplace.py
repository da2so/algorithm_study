
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = collections.Counter()

        for right in range(1, len(s)+1):
            counter[s[right-1]] += 1

            mostk = counter.most_common(1)[0][1]

            if right - left - mostk > k:
                counter[s[left]] -= 1
                left += 1
        return right - left

s = "AABABBA"
k = 1

sol = Solution()
print(sol.characterReplacement(s,k))
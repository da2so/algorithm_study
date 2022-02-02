
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"

sol = Solution()
print(sol.isAnagram(s,t))
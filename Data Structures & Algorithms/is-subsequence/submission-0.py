class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0

        for char in t:
            if count < len(s) and char == s[count]:
                count += 1

        return count == len(s)
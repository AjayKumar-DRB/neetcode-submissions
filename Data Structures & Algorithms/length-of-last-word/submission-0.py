class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_count = 0
        count = 0

        for i in range(len(s)):
            if s[i] == ' ':
                count = 0
            else:
                count += 1
                last_count = count

        return last_count

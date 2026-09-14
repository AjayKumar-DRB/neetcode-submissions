class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strSet = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in strSet:
                strSet.remove(s[left])
                left += 1
            
            strSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
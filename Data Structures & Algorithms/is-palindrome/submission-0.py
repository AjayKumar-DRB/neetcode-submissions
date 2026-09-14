class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedString = []

        for c in s:
            if c.isalnum():
                reversedString.append(c.lower())

        rev = ''.join(reversedString)
        
        return rev == rev[::-1]
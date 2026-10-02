class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ''
        for c in s:
            if c.isdigit() or c.isalpha():
                newString += c.lower()
        
        return newString == newString[::-1]
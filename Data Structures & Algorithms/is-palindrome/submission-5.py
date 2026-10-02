class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) -1

        while left < right:
            while left < len(s) and self.valid_letter(s[left]) == False:
                left += 1
            while right > 0 and self.valid_letter(s[right]) == False:
                right -= 1
            if left < len(s) and right > 0 and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            print(left)
            print(right)

        return True

    def valid_letter(self,c) -> bool:
        return True if c.isalpha() or c.isdigit() else False
        
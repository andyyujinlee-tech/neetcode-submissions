class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        result = 0 

        if len(s) == 1:
            return 1

        seen = set()
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l +=1
            else:
                seen.add(s[r])
                r += 1
            result = max(result, r - l)
        
        return result


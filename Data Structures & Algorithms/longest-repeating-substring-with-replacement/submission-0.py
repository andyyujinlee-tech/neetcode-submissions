class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABAB

        #For each character, what happen if we replace other character with the char c.

        # If the character is equal to the character, we increase the counter.
        # If windwos size - count > k : it means that the we would need to replace chracter more than k time == so the windows is invalid, thus we shrink the window.

        #return max windows.


        charSet = set(s)
        result = 0

        for c in charSet:
            counter = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    counter +=1

                while (r-l+1) - counter > k:
                    if s[l] == c:
                        counter -=1
                    l +=1

                result = max(result, r-l+1)

        return result 









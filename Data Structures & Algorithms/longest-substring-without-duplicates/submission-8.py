class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding windows techniuqe
        # create the set
        # loop through the array
        # if the duplicate found from set , then windows is no longer valid, thus we shrink the windows
        # calculate the current windows size and store max


        l = 0
        result = 0
        duplicate = set()
        for r in range(len(s)):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                l+=1

            duplicate.add(s[r])
            
            result = max(result,r-l+1)
        return result
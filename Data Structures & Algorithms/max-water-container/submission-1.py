class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #calcuate volume
        # min(heights[i],heights[j]) * (j-i)
        l = 0 
        r = len(heights) -1
        result = 0

        while l <= r:
            volume = min(heights[l],heights[r]) * (r-l)
            result = max(volume,result)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        return result 


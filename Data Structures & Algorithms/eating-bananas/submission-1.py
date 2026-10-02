class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #base case, hour = banana
        if len(piles) == h: 
            return max(piles)
        #cannot finish it 
        if sum(piles) <= h:
            return 1

    
        min_k = 1
        #maximum number of k that 
        max_k = max(piles)
        result = max_k

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            time = 0
            for b in piles:
                time += math.ceil(float(b/k))

            if time > h:
                min_k = k + 1
            elif time <= h:
                max_k = k - 1
                result = k
        return result

            
            

            

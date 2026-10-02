class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1

        if len(prices) == 1:
            return 0

        current_max = prices[r] - prices[l]

        while r < len(prices):
            current_max = max(current_max, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r 
            else:
                r += 1
            
        return current_max
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using set to store the value for each iteration ,and if you see the value in the set, return false
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 
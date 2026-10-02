class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force O(n^2)

        dic = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement],i]
            else:
                dic[nums[i]] = i
        return [-1,-1]

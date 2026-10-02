class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # loop through the arry
        # for each loop, you would store the current value and index in dictionary
        # Comput ethe compliment. (target - current Val)
        # check see if the value exist in dictiony

        # if found == return current index + compliment's index 

        num_dic = dict()

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in num_dic:
                return [num_dic[compliment],i]
            num_dic[nums[i]] = i

        return False
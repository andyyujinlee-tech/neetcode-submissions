class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(numbers)):
            dic[numbers[i]] = i
        
        for i in range(len(numbers)):
            temp = target - numbers[i]
            
            if temp in dic:
                return [i+1,dic[temp]+1]
        return []
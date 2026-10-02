class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        
        for i in range(len(numbers)):
            temp = target - numbers[i]

            if dic[temp]:
                return [dic[temp], i+1]
            dic[numbers[i]] = i +1

        return []
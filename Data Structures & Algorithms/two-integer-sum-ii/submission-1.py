class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            temp = target - numbers[i]
        
            #binary search from i+1 to end
            l = i + 1
            r = len(numbers) - 1
            

            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == temp:
                    return [i+1,mid+1]
                elif numbers[mid] < temp:
                    l = mid +1
                else:
                    r = mid -1
        return [-999,-999]



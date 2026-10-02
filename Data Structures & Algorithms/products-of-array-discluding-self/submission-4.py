class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        is_zero = False
        zero_count = 0
        for num in nums:
            if num != 0:
                total = num * total
            else:
                is_zero = True
                zero_count = zero_count + 1
                pass

        for i in range(len(nums)):
            if is_zero == False:
                nums[i] = total // nums[i]
            else:
                print(zero_count)
                if nums[i] == 0 and zero_count <= 1:
                    nums[i] = total
                else:
                    nums[i] = 0
        
        return nums
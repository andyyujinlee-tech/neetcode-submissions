class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        duplicate_check = set()
        # -4 -1 -1 0 1 2 

        for i in range(len(nums)):
            l = i+1
            r = len(nums) -1

            target = -(nums[i])
    
            while l <=r:
                s = nums[l] + nums[r]
                found = tuple(sorted([nums[i], nums[l], nums[r]]))
                if s == target and l !=r and found not in duplicate_check:
                    result.append(found)
                    duplicate_check.add(found)
                    l = l +1
                    r = r -1 
                elif s > target:
                    r = r - 1
                else:
                    l = l + 1
        return result
        
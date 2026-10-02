class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the minimum or the piviot

        #perfrom two binary search one from l = 0 to r= until piviot , other l = until privot +1 to r = len -1

        #find minimum
        l = 0 
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        #find the mimum point
        l1 = 0
        r1 = l -1

        result = self.binary_search(l1,r1,nums,target)
        if result != -1:
            return result

        l2 = l
        r2 = len(nums) - 1

        result = self.binary_search(l2,r2,nums,target)
        return result

    def binary_search(self,l,r,nums,target):
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        

        
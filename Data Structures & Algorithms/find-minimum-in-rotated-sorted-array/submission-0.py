class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1 

        if nums[lo] < nums[hi]: 
            return nums[0]


        while lo < hi: 

            mid = (hi + lo) // 2
        
            if nums[mid] > nums[hi]:
                lo = mid + 1 
            else: 
                hi = mid 

        return nums[lo]
                    

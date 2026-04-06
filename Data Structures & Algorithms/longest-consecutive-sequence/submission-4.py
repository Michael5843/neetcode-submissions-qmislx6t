class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_count = 0
        for num in nums:
            if num-1 in nums: 
                continue
            
            temp = num+1
            count = 1
            while temp in nums: 
                count += 1 
                temp += 1 
            max_count = max(max_count, count) 

        return max_count




            
  

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        seen = set([]) 
        max_count = 0
        for num in nums:
            seen.add(num)
            if num-1 in seen: 
                continue
            
            temp = num+1
            count = 1
            while temp in seen or temp in nums: 
                count += 1 
                temp += 1 
            max_count = max(max_count, count) 

        return max_count




            
  

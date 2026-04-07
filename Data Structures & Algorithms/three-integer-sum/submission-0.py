class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        results = []
        seen = set()

        for i in range(len(nums)): 
            if i < len(nums) - 1 :
                left = i + 1 
            else: 
                continue
            
            right = len(nums) - 1 

            while left < right: 
                value = nums[left] + nums[right] + nums[i]
                if value == 0: 
                    triplet = (nums[left], nums[right], nums[i])
                    
                    if triplet not in seen: 
                        seen.add(triplet) 
                        results.append(list(triplet))

                    left += 1 
                    right -= 1
                    
                    
                    #while left < right and nums[left] == nums[left + 1]: 
                    #    left += 1 
                    #while left < right and nums[right] == nums[right - 1]: 
                    #    right -= 1
                    #left += 1 
                    # right -= 1 

                elif value < 0: 
                    left += 1
                else: 
                    right -= 1
        
        return results

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)

        for i in range(len(nums)): 
            temp = 1
            for k in range(len(nums)): 
                if k == i: 
                    continue
                temp *= nums[k]
            products[i] = temp

        return products
                
            
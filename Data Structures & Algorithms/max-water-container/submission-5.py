class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1 

        while left < right: 
            left_num = heights[left]
            right_num = heights[right]

            max_area = max(max_area, min(left_num, right_num) * (right - left))

            if left_num < right_num: 
                left += 1
            else:
                right -= 1 

            
        
        return max_area
            


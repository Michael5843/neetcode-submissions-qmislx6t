class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures): 
            while stack and temperatures[stack[-1]] < temp: 
                result[stack.pop()] = idx - stack[-1] 
            
            stack.append(idx)
        
        return result

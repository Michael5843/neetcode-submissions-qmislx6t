class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        operators = ['+', '-', '*', '/'] 

        for token in tokens: 
            if token in operators: 
                a = int(stack.pop())
                match token: 
                    case '+': 
                        stack[-1] = int(stack[-1]) + a
                    case '-': 
                        stack[-1] = int(stack[-1]) - a
                    case '*': 
                        stack[-1] = int(stack[-1]) * a
                    case '/': 
                        stack[-1] = int(stack[-1]) / a
            else: 
                stack.append(token)
        return int(stack.pop()) 
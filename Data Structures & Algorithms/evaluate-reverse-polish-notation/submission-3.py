class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        operators = ['+', '-', '*', '/'] 

        for token in tokens: 
            if token in operators: 
                a, b = int(stack.pop()), int(stack.pop())
                match token: 
                    case '+': 
                       stack.append(b + a)
                    case '-': 
                        stack.append(b - a)
                    case '*': 
                        stack.append(b * a)
                    case '/': 
                        stack.append(b / a)
            else: 
                stack.append(token)
        return int(stack.pop()) 
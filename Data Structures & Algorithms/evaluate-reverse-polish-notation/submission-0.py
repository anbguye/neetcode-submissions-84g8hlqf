class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(num_1 - num_2)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(int(num_1 / num_2))
            else:
                stack.append(int(token))
        
        return stack[-1]
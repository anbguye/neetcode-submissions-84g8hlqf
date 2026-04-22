class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        res = 0

        for n in operations:

            if n == "C":
                stack.pop()
            elif n == "+":
                stack.append(stack[-1] + stack[-2])
            elif n == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(n))

        while stack:
            res += stack.pop()

        return res
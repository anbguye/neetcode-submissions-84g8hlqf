class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1
        
        steps = [0, 1]

        i = 0

        while i <= n:
            temp = steps[1]
            steps[1] = steps[0] + temp
            steps[0] = temp
            i += 1
        
        return steps[0]
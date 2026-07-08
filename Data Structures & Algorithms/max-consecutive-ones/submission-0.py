class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        curr = 0
        
        for n in nums:
            
            if n == 1:
                curr += 1
                res = max(curr, res)
            else:
                curr = 0
        
        return res
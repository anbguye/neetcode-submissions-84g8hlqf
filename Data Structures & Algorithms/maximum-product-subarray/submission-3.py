class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        currMin = 1
        currMax = 1

        for n in nums:

            tmp = n * currMax

            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, tmp, n * currMin)

            res = max(res, currMax)
        
        return res
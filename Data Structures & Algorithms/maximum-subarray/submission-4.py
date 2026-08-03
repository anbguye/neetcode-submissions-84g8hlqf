class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        res = float('-inf')
        currSum = float('-inf')

        for n in nums:

            if currSum < 0:
                currSum = n
            else:
                currSum += n
            res = max(res, currSum)

        return res
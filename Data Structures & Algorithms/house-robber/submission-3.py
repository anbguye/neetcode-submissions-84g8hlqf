class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) -1, -1, -1):
            
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        print(dp)
        return max(dp[0], dp[1]) if len(dp) > 1 else dp[0]
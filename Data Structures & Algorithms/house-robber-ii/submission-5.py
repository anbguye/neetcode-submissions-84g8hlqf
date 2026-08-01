class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def robbing(houses):

            dp = [0] * (len(houses) + 2)

            for i in range(len(houses) - 1, -1, -1):

                dp[i] = max(houses[i] + dp[i + 2], dp[i + 1])
            
            return dp[0]
        
        choice_1 = robbing(nums[1:])
        choice_2 = robbing(nums[:-1])

        return max(choice_1, choice_2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_sum = [1] * (len(nums))

        pre = 1

        for i in range(len(nums)):
            total_sum[i] *= pre
            pre *= nums[i]
        
        post = 1

        for i in range(len(nums) -1, -1, -1):
            total_sum[i] *= post
            post *= nums[i]
        
        return total_sum
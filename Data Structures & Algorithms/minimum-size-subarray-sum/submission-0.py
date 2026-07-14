class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0
        l = 0
        best_length = 0

        for r in range(len(nums)):

            total += nums[r]

            while total >= target:

                if best_length == 0:
                    best_length = (r - l + 1)

                best_length = min(best_length, (r - l + 1))
                total -= nums[l]
                l += 1
        
        return best_length
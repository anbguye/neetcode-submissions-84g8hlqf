class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)
        prefix_array = [0] * (n + 1)
        total = 0

        for i in range(n):
            total += nums[i]
            prefix_array[i] = total
        
        prefix_array[n] = total

        for i in range(n):

            leftSum = prefix_array[i - 1] if i > 0 else 0
            rightSum = prefix_array[n] - prefix_array[i]
            if leftSum == rightSum:
                return i

        return -1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 2

        for r in range(2, len(nums)):

            if nums[l - 2] != nums[r] or nums[l - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        
        return l
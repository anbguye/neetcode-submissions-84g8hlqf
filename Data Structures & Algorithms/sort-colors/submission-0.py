class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0

        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1
        
        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red -= 1
            elif white:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
                blue -=1
        
        return nums
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):

            smallest_idx = i

            for j in range(i, len(nums)):
                
                if nums[j] < nums[smallest_idx]:
                    smallest_idx = j

            if nums[i] > nums[smallest_idx]:
                nums[smallest_idx], nums[i] = nums[i], nums[smallest_idx]

        return nums

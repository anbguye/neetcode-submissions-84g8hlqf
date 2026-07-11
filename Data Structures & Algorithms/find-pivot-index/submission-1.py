class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_array = []
        total = 0
        
        for n in nums:
            total += n
            prefix_array.append(total)
        
        for i in range(len(prefix_array)):
            leftSum = prefix_array[i - 1] if i > 0 else 0
            rightSum = total - prefix_array[i]
            if leftSum == rightSum:
                return i
        
        return -1
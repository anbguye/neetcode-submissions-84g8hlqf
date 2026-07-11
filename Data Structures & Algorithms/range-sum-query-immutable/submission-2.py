class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.preSum = []

        for n in nums:
            total += n
            self.preSum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preLeft = self.preSum[left - 1] if left - 1 >= 0 else 0
        preRight = self.preSum[right]
        return preRight - preLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
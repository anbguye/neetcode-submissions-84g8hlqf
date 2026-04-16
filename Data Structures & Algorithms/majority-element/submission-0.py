class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_val = None
        cnt = -1

        for n in nums:
            if cnt == -1 or curr_val == n:
                curr_val = n
                cnt += 1
            else:
                cnt -=1

        return curr_val
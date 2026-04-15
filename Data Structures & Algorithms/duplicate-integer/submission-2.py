class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        digits_stored = set()

        for n in nums:
            if n not in digits_stored:
                digits_stored.add(n)
            else:
                return True
        
        return False
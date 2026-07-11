class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set()

        for n in nums:
            nums_set.add(n)
        
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr = 0

                while curr + n in nums_set:
                    curr += 1
                
                longest = max(longest, curr)
        
        return longest

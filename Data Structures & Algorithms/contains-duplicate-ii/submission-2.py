class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        stored = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                stored.remove(nums[l])
                l += 1

            if nums[r] in stored:
                return True
            
            stored.add(nums[r])
                
        return False
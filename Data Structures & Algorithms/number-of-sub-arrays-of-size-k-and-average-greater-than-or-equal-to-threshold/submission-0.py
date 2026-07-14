class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        total = 0
        l = 0
        res = 0

        for r in range(len(arr)):

            total += arr[r]

            if r - l + 1 > k:
                total -= arr[l]
                l += 1
                
            if (r - l + 1) == k:
                res += 1 if (total / k) >= threshold else 0

        return res
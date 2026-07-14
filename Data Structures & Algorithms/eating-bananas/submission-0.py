class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        best = r
        
        while l <= r:

            mid = (l + r) // 2
            time = 0

            for n in piles:
                time += math.ceil(n / mid)
            
            if time > h:
                l = mid + 1
            else:
                best = mid
                r = mid - 1


        return best

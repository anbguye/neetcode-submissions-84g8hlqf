from _heapq import heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            val1 = heapq.heappop(stones) * -1
            val2 = heapq.heappop(stones) * -1

            res = abs(val1 - val2)

            if res > 0:
                heapq.heappush(stones, -res)

        return -stones[0] if stones else 0
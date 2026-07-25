class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        heapq.heapify(minHeap)

        for x, y in points:
            
            dist = math.sqrt((x**2) + (y **2))
            heapq.heappush(minHeap, [dist, [x, y]])

        res = []

        while len(res) < k:

            res.append(heapq.heappop(minHeap)[1])

        return res

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_seen = -1

        for i in range(len(arr) - 1, -1, -1):
            
            arr[i], max_seen = max_seen, max(arr[i], max_seen)
        
        return arr
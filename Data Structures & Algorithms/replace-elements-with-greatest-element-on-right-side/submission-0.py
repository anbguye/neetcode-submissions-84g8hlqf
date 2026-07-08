class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            
            highest = -1

            for j in range(i + 1, len(arr)):

                if arr[j] > highest:
                    highest = arr[j]
            
            arr[i] = highest

        return arr
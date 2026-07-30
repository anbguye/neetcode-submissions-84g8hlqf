class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        count = Counter(nums)

        def dfs():

            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    
                    subset.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    subset.pop()
        
        dfs()
        return res

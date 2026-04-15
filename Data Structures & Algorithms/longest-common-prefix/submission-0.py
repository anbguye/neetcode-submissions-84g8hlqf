class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if not strs:
            return res

        for i in range(len(strs[0])):

            curr = strs[0][i]

            for word in strs:
                if i > len(word) - 1 or word[i] != curr:
                    return res
            
            res += curr
        
        return res
                


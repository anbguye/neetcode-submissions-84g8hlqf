class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_counter = defaultdict(int)
        res = 0
        maxf = 0
        l = 0

        for r in range(len(s)):

            freq_counter[s[r]] += 1
            maxf = max(maxf, freq_counter[s[r]])

            while (r - l + 1) - maxf > k:
                freq_counter[s[l]] -= 1
                l += 1
            
            res = (r - l + 1)
        
        return res

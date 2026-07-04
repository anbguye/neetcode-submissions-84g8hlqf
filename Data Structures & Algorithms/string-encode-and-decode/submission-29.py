class Solution:

    # 5#Hello5#World
    # i
    # j
    # i j
    #   i    j
    #         ji
    #          i    j

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []
        word_len = 0

        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            i = j + 1
            j = i + word_len
            res.append(s[i:j])
            i = j
        return res
            



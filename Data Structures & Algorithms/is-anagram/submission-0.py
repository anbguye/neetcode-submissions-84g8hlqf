class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stored_lets = defaultdict(int)

        for let in s:
            stored_lets[let] += 1
        for let in t:
            stored_lets[let] -= 1

        print(stored_lets)
        
        for v in stored_lets.values():
            if v != 0:
                return False
        
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        
        stored = []
        sheet = {")":"(", "}":"{", "]":"["}

        for let in s:
            if let in sheet.values():
                stored.append(let)
            elif not stored or stored.pop() != sheet[let]:
                return False
        
        return not stored
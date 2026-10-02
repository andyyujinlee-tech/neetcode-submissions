class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        pattern = {")":"(", "}":"{","]":"["}


        if s[0] not in ("(", "[", "{"):
            return False

        for c in s:
            if c in pattern.values():
                q.append(c)
            elif c in pattern:
                if len(q) == 0:
                    return False 
                temp = q.pop()
                if pattern.get(c) != temp:
                    return False
            else: 
                return False
        
        if len(q) != 0:
            return False
        return True 

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        
        parentheses = {"{" : "}", "[" : "]" , "(" : ")"}

        for c in s:
            if c in parentheses:
                q.append(c)
            elif c in parentheses.values() and len(q) > 0:
                temp = q.pop()
                # {
                if parentheses[temp] != c:
                    return False
            else:
                return False
        
        return len(q) == 0


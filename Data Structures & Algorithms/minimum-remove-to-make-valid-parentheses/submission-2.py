class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = ''
        closed = s.count(')')

        for ch in s:
            if ch == ')':
                if stack:
                    stack.pop()
                    res += ch
                else:
                    closed -= 1

            elif ch == '(':
                if closed > 0:
                    stack.append(ch)
                    res += ch
                    closed -= 1
            
            else:
                res += ch
        
        return res


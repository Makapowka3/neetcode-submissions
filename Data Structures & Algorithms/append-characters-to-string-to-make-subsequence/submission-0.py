class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #kind of a stack
        #pop 1 by 1
        #append len(stack)

        stack = []
        for ch in t:
            stack.append(ch)
        stack.reverse()

        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
        
        return len(stack)
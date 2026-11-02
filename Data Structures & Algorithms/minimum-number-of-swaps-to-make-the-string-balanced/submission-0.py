class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        count = 0
        for ch in s:
            if ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)

            else:
                stack.append(ch)

        return (len(stack) // 2) // 2 + (len(stack) // 2) % 2
        

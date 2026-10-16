class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for l in logs:
            if l == '../':
                if stack:
                    stack.pop()
            elif l == './':
                pass
            else:
                stack.append(1)

        return len(stack)
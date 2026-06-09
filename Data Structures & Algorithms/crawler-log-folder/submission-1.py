class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if not stack:
                if log != './' and log != '../':
                    stack.append(log)
            else:
                if log == '../':
                    stack.pop()
                elif log != './':
                    stack.append(log)
        return len(stack)
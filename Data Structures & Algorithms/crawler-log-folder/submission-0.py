class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for move in logs:
            if move == '../':
                if stack:
                    stack.pop()
            elif move == './':
                pass
            else:
                stack.append(1)


        return len(stack)
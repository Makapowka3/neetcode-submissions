class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for op in path:
            if op:
                if op == '..' :
                    if stack:
                        stack.pop()
                elif op == '.':
                    continue
                else:
                    stack.append(op)
        return '/' + '/'.join(stack)
        
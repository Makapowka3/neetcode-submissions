class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif op == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif op == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif op == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                stack.append(int(op))
        return stack[0]
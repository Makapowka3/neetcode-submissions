class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        new = []
        num = ""

        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                if num:
                    new.append(num)
                    num = ""

                new.append(ch)

        if num:
            new.append(num)
        
        stack = []
        for ch in new:
            if ch not in {'+','-','*','/'} and stack:
                if stack[-1] == '*' or stack[-1] == '/':
                    operator = stack.pop()
                    second = stack.pop()

                    if operator == '*':
                        stack.append(int(ch) * int(second))
                    else:
                        stack.append(int(second) // int(ch))
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        res = 0
        operator = '+'
        for i in range(len(stack)):
            if stack[i] in {'+','-'}:
                if stack[i] == '+':
                    operator = '+'
                else:
                    operator = '-'
            else:
                if operator == '+':
                    res += int(stack[i])
                else:
                    res -= int(stack[i])
        
        return res
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ''

        res = ''
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                if num[i]*3 > res:
                    res = num[i]*3
        return res
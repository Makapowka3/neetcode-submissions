class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ''

        res = -1
        for i in range(2, len(num)):
            if num[i-2] == num[i-1] == num[i]:
                if int(num[i]*3) > int(res):
                    res = num[i]*3
        
        if res == -1:
            return ''
        return str(res)
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                res = max(res, int(num[i]*3))

        if res == -1:
            return ''
        elif res == 0:
            return '000'
        
        return str(res)
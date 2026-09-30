class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if int(num[i]) > res:
                    res = int(num[i])
        
        if res == -1:
            return ''

        return str(res) * 3
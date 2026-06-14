class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        streak = 0
        for i in range(1, len(num)):
            if streak > 2:
                res = max(res, int(f'{num[i-1]*3}'))
            if num[i-1] == num[i]:
                if streak:
                    streak += 1
                else:
                    streak = 2
            else:
                streak = 0
        if streak > 2:
            res = max(res, int(f'{num[i-1]*3}'))
        if res == -1:
            return ''
        elif res == 0:
            return '000'
        return str(res)
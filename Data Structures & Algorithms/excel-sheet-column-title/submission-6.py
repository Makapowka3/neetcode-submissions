class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        coll = []
        temp = columnNumber
        base = ord('A')
        while  temp // 26 > 0:
            coll.append((temp-1)%26)
            temp = (temp - 1) // 26
        if temp != 0:
            coll.append(temp - 1)
        coll.reverse()
        for v in coll:
            res.append(chr(base + v))
        return ''.join(res)

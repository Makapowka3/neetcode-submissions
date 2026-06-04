class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        current = 0
        while current != numRows - 1:
            res.append(res[current][:])
            res[current+1].append(1)
            if len(res[current+1]) > 2:
                i,j = 0, 1
                while j < len(res[current]):
                    res[current+1][j] = res[current][i] + res[current][j]
                    i += 1
                    j += 1
            current += 1
        return res
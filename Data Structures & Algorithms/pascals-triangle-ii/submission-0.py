class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(1, rowIndex+1):
            new_el = [1]

            j = 1
            while j < len(res[i-1]):
                new_el.append(res[i-1][j] + res[i-1][j-1])
                j += 1

            new_el.append(1)
            res.append(new_el)
            
        return res[-1]
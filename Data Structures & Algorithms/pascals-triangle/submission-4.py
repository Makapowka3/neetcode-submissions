class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows -1):
            temp_row = res[i].copy()
            temp_row.append(1)

            p1, p2 = 0, 1
            next_row = temp_row.copy()
            while p2 < len(next_row)-1:
                next_row[p2] = temp_row[p2] + temp_row[p1]
                p1 += 1
                p2 += 1
            
            res.append(next_row)
        
        return res
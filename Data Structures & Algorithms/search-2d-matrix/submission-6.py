class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lower, upper = 0, (m * n) - 1
        print(m*n)
        while lower <= upper:
            middle = (lower + upper) // 2
            row = middle // n
            column = middle % n
            print(row,column, 'r')
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                lower = middle + 1
            else:
                upper = middle - 1
        return False
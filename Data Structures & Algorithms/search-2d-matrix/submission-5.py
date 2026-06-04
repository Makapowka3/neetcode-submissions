class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lower, upper = 0, m * n
        print(m*n)
        while lower <= upper:
            middle = (lower + upper) // 2
            row = middle // n
            column = middle % n
            if row+1 > m or column+1 > n:
                return False
            print(row,column, 'r')
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                lower = middle + 1
            else:
                upper = middle - 1
        return False
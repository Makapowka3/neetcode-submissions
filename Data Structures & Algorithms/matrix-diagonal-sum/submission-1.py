class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)

        sum1, sum2 = 0,0
        for i in range(len(mat)):
            sum1 += mat[i][i]
            sum2 += mat[i][dim-i-1]
        
        if dim % 2 == 0:
            return sum1 + sum2
        
        return sum1 + sum2 - mat[dim//2][dim//2]

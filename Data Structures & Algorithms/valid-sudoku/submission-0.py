class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    if board[row][column] in rows[row]:
                        return False
                    else:
                        rows[row].add(board[row][column])
                    if board[row][column] in cols[column]:
                        return False
                    else:
                        cols[column].add(board[row][column])
                    if board[row][column] in boxes[(row // 3)*3 + (column // 3)]:
                        return False
                    else:
                        boxes[(row // 3)*3 + (column // 3)].add(board[row][column])
        return True
        


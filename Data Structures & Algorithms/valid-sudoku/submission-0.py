class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            filtered = [x for x in row if x != "."]
            if len(filtered) != len(set(filtered)):
                return False

        # Check columns
        for col in range(9):
            filtered = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(filtered) != len(set(filtered)):
                return False

        # Check 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                filtered = [
                    board[r][c]
                    for r in range(box_row * 3, box_row * 3 + 3)
                    for c in range(box_col * 3, box_col * 3 + 3)
                    if board[r][c] != "."
                ]
                if len(filtered) != len(set(filtered)):
                    return False

        return True

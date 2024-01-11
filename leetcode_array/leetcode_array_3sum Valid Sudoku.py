class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 檢查每一行
        for i in range(9):
            if not self.is_valid_unit(board[i]):
                return False

        # 檢查每一列
        for i in range(9):
            if not self.is_valid_unit([board[j][i] for j in range(9)]):
                return False

        # 檢查每一個 3x3 子區域
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_unit([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                    return False

        return True

    def is_valid_unit(self, unit):
        seen = set()
        for num in unit:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True
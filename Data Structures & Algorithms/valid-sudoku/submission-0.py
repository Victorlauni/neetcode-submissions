class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        grids = [set() for i in range(9)]
        for rowInd, row in enumerate(board):
            for colInd, col in enumerate(row):
                if col == '.': continue
                grid = 3*(rowInd//3) + (colInd//3)
                if col in rows[rowInd]:
                    print(rows)
                    return False
                if col in cols[colInd]:
                    print(cols)
                    return False
                if col in grids[grid]:
                    print(grids)
                    return False
                rows[rowInd].add(col)
                cols[colInd].add(col)
                grids[grid].add(col)
        return True

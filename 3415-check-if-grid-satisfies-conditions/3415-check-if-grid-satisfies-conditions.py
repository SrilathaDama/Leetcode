class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        prev = -1
        count = 0
        for c in range(col):
            colVal = grid[0][c]
            for r in range(1,row):
                if grid[r][c] != colVal:
                    return False
            if prev == colVal:
                return False
            prev = colVal
        return True
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row , col = len(rowSum), len(colSum)
        arr = [[0] * col for _ in range(row)]

        i, j = 0,0
        while i < row and j < col:
            x = min(rowSum[i], colSum[j])
            arr[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            i += (rowSum[i] == 0)
            j += (colSum[j] == 0)
        return arr 
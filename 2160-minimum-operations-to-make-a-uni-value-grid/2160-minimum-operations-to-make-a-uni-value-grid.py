class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        g = []
        for l in grid: g += l
        g.sort()
        m, result = g[len(g) // 2], 0
        for num in g:
            d = abs(num - m)
            if d % x: return -1
            result += d // x
        return result
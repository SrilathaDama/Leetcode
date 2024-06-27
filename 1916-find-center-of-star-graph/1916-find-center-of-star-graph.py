class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return mode(e[0]+e[1])
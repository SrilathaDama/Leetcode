class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        arr = [(i+1) for i in range(n)]
        i=0
        while time > 0:
            while time > 0 and i < len(arr)-1:
                i += 1
                time -= 1
            while time > 0 and i > 0:
                i -= 1
                time -= 1
        return arr[i]
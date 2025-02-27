class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            if a*a + b*b == c:
                return True
            elif a*a + b*b > c:
                b -= 1
            else:
                a += 1

        return False
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a, b = bin(num1).count('1'), bin(num2).count('1')
        diff = abs(a - b)
        res = num1

        if a > b:
            for i in range(32):
                if diff == 0:
                    break
                if (1 << i) & num1 > 0:
                    res ^= 1 << i
                    diff -= 1
        elif a < b:
            for i in range(32):
                if diff == 0:
                    break
                if (1 << i) & num1 == 0:
                    res ^= 1 << i
                    diff -= 1

        return res
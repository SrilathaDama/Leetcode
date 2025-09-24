class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        integer = n // d
        rem = n % d
        if rem == 0:
            return sign + str(integer)

        res = [sign + str(integer), "."]
        seen = {}

        while rem != 0:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, "(")
                res.append(")")
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return "".join(res)
class Solution:
    def reverse(self, x: int) -> int:
        revnum=0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        neg = x < 0
        x = abs(x)
        while x>0:
            lastdigit = x%10
            x = x//10
            revnum = (revnum * 10) + lastdigit

        if neg:
            revnum= -revnum
        
        if revnum < INT_MIN or revnum > INT_MAX:
            return 0
        
        return revnum

        
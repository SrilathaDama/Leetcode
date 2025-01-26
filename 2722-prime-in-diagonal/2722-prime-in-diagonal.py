class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        op=0
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        for i in range(len(nums)):
            
            if is_prime(nums[i][i]):
                op=max(op,nums[i][i])
            if is_prime(nums[i][len(nums)-i-1]):
                op=max(op,nums[i][len(nums)-i-1])
        return op

        
        
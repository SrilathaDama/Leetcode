class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7

        cache = {}
        def dfs(mask, prev):
            if mask == (1 << N) - 1:
                return 1

            if (mask, prev) in cache:
                return cache[(mask, prev)]

            total = 0

            for i in range(N):

                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    total += dfs(mask | (1 << i), nums[i])


            cache[(mask, prev)] = total % MOD
            return total % MOD

        return dfs(0, 1)
        
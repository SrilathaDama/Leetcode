class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        def solve(i, r):
            if i < 0:
                if r == 0:
                    return 0
                else:
                    return -float("inf")
            if (i, r) in dp:
                return dp[(i, r)]
            notpick = 0 + solve(i - 1, r)
            new_r = (r + nums[i]) % 3
            pick = nums[i] + solve(i - 1, new_r)
            dp[(i, r)] = max(pick, notpick)
            return dp[(i, r)]
        dp = {}
        return solve(len(nums) - 1, 0)
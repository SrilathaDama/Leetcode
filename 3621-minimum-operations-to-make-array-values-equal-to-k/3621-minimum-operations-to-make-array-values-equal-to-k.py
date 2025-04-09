class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in set(nums):
            if i > k:
                res += 1
            elif i < k:
                return -1
        if len(set(nums)) == 1 and nums[0] == k:
            return 0
        return res
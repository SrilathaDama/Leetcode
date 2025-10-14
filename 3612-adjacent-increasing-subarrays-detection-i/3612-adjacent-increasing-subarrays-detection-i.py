class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cur = 0
        pk = 0
        for i, x in enumerate(nums):
            if i == 0 or nums[i - 1] < x:
                cur += 1
            else:
                pk = int(k <= cur)
                cur = 1
                
            if pk and k <= cur:
                return True
            if k * 2 <= cur:
                return True

        return False
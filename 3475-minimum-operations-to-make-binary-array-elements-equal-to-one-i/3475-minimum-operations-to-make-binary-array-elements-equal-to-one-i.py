class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1
        return count if (nums[len(nums)-1] == 1 and nums[len(nums)-2]==1) else -1 
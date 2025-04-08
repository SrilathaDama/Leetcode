class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seenSet = set()
        removal = 0
        i = 0
        while i < len(nums):
            if nums[i] in seenSet:
                seenSet = set()
                removal += 1
                i = 0
                nums = nums[3:]
            else:
                seenSet.add(nums[i])
                i += 1
        return removal
        
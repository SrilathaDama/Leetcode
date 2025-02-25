class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        while left < n - 1 and nums[left + 1] >= nums[left]:
            left += 1
        if left == n - 1:
            return 0
        right = n - 1

        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1

        arr_max = max(nums[left: right + 1])
        arr_min = min(nums[left: right + 1])

        while left > 0 and nums[left - 1] > arr_min:
            left -= 1
        while right + 1 < n and nums[right + 1] < arr_max:
            right += 1

        return right - left + 1
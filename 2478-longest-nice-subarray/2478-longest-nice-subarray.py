class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        longest = 0
        current_summ = 0
        
        for right in range(len(nums)):
            while left < right and current_summ + nums[right] != (current_summ | nums[right]):
                current_summ -= nums[left]
                left += 1
            
            current_summ += nums[right]
            
            longest = max(longest, right - left + 1)
        
        return longest
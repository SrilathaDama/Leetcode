class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum |= num
        
        n = len(nums)
        x = 2**(n -1)
        return total_sum * x
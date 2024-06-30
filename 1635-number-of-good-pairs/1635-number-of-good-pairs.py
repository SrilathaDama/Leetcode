class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0] * 101  
        count = 0
        for num in nums:
            count += freq[num]
            freq[num] += 1
        return count
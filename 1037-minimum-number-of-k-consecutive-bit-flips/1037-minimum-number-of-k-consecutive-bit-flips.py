class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)
        flipsincurrwindow=0
        flips=0

        for i in range (len(nums)):
            if i>=k:
                if flipped[i-k]:
                    flipsincurrwindow-=1
            if flipsincurrwindow % 2 == nums[i]:
                if i+k > len(nums):
                    return -1
                flipsincurrwindow +=1
                flipped[i] = True
                flips+=1
        return flips
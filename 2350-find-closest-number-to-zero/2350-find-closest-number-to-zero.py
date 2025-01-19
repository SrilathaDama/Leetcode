class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closestnum = nums[0]
        for num in nums:
            if abs(num) < abs(closestnum):
                closestnum = num

        if closestnum < 0 and abs(closestnum) in nums:
            return abs(closestnum)
        else:
            return closestnum
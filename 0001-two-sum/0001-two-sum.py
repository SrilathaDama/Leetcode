class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,j in enumerate(nums):
            diff = target - nums[i]

            if diff in dict:
                return [i, dict[diff]]
            else:
                dict[j] = i
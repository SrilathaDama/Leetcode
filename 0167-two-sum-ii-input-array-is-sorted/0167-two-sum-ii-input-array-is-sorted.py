class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,j in enumerate(nums):
            diff = target - nums[i]

            if diff in dict:
                return [dict[diff]+1, i+1]
            else:
                dict[j] = i
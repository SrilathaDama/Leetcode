class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums== []:
            return []

        res = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == res[-1][-1] + 1:
                res[-1][-1] = nums[i]
            else:
                res.append([nums[i], nums[i]])
            
        res_str = []
        for interval in res:
            if interval[0] == interval[1]:
                res_str.append(str(interval[0]))
            else:
                res_str.append(str(interval[0]) + '->' + str(interval[1]))
        return res_str
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dictionary = {}

        for i in nums:
            dictionary[i] = i
        
        i = 1
        while(True):
            try:
                dictionary[i]
            except:
                return i
            i +=1 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        num_count={}
        for i in nums:
            if i in num_count:
                count+= num_count[i]
                num_count[i] +=1
            else:
                num_count[i] =1
            
        return count
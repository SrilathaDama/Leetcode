class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        map = [0] * k
        map[0] = 1

        for num in nums:
            prefix = (prefix + num % k) % k
            res += map[prefix]
            map[prefix] += 1
        
        return res
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = Counter()
        cur = 0
        i = 0
        res = 0
        for num in nums:
            cur += counter[num]
            counter[num] += 1
            while cur >= k:
                cur -= counter[nums[i]]-1
                counter[nums[i]] -= 1
                i += 1
            res += i
        return res
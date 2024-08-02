class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        n = len(nums)

        ans = count1 = sum(nums[:sum_])

        for i in range(sum_, n+sum_):
            count1 += nums[i%n]

            count1 -= nums[(i - sum_ + n)%n]

            ans = max(ans,count1)
        
        return sum_ - ans
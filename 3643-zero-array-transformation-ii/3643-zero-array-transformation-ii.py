class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        prefix = [0] * (n + 1)

        k, cur = 0, 0

        for index in range(n):
            while cur + prefix[index] < nums[index]:
                if k == m:
                    return -1

                l, r, val = queries[k]
                k += 1

                if index > r:
                    continue

                if index > l:
                    l = index

                prefix[l] += val
                prefix[r + 1] -= val

            cur += prefix[index]

        return k
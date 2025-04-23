class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = defaultdict(int)
        for i in range(1, n + 1):
            val = sum(int(d) for d in str(i))
            res[val] += 1

        max_count = max(res.values())
        return list(res.values()).count(max_count)


        
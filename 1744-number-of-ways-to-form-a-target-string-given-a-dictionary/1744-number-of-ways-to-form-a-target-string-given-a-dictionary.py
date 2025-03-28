class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        M = int(1e9) + 7
        count = defaultdict(int)

        for word in words:
            for i in range(len(word)):
                count[i, word[i]] += 1
        
        @lru_cache(None)
        def fn(i: int, j: int) -> int:
            if i == len(target): return 1
            if j == len(words[0]): return 0

            # form by ignoring jth index
            ans = fn(i, j + 1) % M

            # form by taking at jth index
            ans = (ans + count[j, target[i]] * fn(i + 1, j + 1)) % M

            return ans
        
        return fn(0, 0)
        
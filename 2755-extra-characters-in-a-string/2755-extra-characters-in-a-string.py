class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [1e9] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for word in dictionary:
                if (n - i >= len(word) and s[i:i+len(word)] == word):
                    dp[i+len(word)] = min(dp[i+len(word)], dp[i])
            dp[i+1] = min(dp[i+1], dp[i] + 1)
        return dp[n]

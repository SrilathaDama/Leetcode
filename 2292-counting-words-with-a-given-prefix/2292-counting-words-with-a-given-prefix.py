class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for item in words:
            if item.startswith(pref):
                ans += 1

        return ans
        
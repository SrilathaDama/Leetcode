class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_, max_ = min(strs), max(strs)

        for i in range(len(min_)):
            if min_[i] != max_[i]:
                return min_[:i]
        return min_
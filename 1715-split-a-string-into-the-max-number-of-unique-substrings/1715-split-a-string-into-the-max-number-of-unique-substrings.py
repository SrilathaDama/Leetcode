class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return len(seen)
            max_splits = 0
            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, backtrack(i, seen))
                    seen.remove(substring)
            return max_splits
        
        return backtrack(0, set())
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        letter_count = {}
        for ch in s:
            letter_count[ch] = letter_count.get(ch, 0) + 1
        odd_count = 0
        for cnt in letter_count.values():
            if cnt % 2:
                odd_count += 1
        return odd_count <= k
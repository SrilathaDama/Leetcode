class Solution:
    def minimumDeletions(self, s: str) -> int:
        bcount = 0
        deletions = 0
        for char in s:
            if char == 'a':
                deletions = min(deletions + 1, bcount)
            else:
                bcount += 1
        
        return deletions
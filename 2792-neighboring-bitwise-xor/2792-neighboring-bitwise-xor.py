class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        output: int = 0
        for num in derived:
            output ^= num
        return not output
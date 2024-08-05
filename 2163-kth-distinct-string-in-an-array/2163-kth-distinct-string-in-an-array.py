class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for s, f in Counter(arr).items():
            if f == 1:
                k -= 1
                if not k: return s
        return ""
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        swap_index = [i for i in range(len(s1)) if s1[i] != s2[i]]

        return len(swap_index) == 2 and (
            s1[swap_index[0]] == s2[swap_index[1]] and s1[swap_index[1]] == s2[swap_index[0]]
        )
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        add = [0] * (n + 2)
        add[1] = 1
        know, share = 1, 0
        for i in range(2, n + 1):
            if i - delay >= 1:
                share = (share + add[i - delay]) % (10**9 + 7)
            if i - forget >= 1:
                share = (share - add[i - forget]) % (10**9 + 7)
            add[i] = share % (10**9 + 7)
            know = (know + add[i]) % (10**9 + 7)
            if i - forget >= 1:
                know = (know - add[i - forget]) % (10**9 + 7)
        return know % (10**9 + 7)
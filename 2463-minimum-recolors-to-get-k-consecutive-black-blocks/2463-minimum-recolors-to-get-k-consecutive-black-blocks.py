class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        last = 0
        max_black = 0
        black = 0
        for i in range(len(blocks)):
            if blocks[i] == 'B':
                black += 1

            if i - last == k-1:
                max_black = max(max_black, black)
                if blocks[last] == 'B':
                    black -= 1
                last += 1
        
        return k - max_black
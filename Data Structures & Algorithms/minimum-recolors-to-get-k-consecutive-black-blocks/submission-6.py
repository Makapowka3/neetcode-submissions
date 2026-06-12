class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        p1 = 0

        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        min_whites = white
        for b in blocks[k:]:
            if b == 'W':
                white += 1
            if blocks[p1] == 'W':
                white -= 1
            p1 += 1
            min_whites = min(min_whites, white)
        
        return min_whites
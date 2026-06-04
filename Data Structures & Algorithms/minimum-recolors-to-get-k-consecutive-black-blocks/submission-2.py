class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        p1, p2 = 0, 0
        white_count = 0
        while p2 != k:
            if blocks[p2] == 'W':
                white_count += 1
            p2 += 1
        min_count = white_count
        
        while p2 < len(blocks):
            if blocks[p2] == 'W':
                white_count += 1
            if blocks[p1] == 'W':
                white_count -= 1
            min_count = min(min_count, white_count)
            p2 += 1
            p1 += 1
        
        return min_count
            
                
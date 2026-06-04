class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        min_run = upper
        while lower <= upper:
            middle = (lower + upper) // 2
            running = 0
            for banana in piles:
                running += (banana + middle - 1) // middle
            if running > h:
                lower = middle + 1
            else:
                upper = middle - 1
                min_run = min(min_run, middle)

        return min_run
            
            
                
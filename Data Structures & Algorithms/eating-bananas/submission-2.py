class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 0, sum(piles)
        min_run = sum(piles)
        while lower <= upper:
            middle = (lower + upper) // 2
            running = 0
            for banana in piles:
                if banana % middle == 0:
                    running += banana / middle
                else:
                    running += (banana // middle) + 1
                running = int(running)
            if running > h:
                lower = middle + 1
            else:
                upper = middle - 1
                min_run = min(min_run, middle)
            if (lower + upper) // 2 == 0:
                return min_run

        return min_run
            
            
                
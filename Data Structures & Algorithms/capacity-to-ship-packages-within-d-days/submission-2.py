class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower_cap, upper_cap = max(weights), sum(weights)
        min_cap = upper_cap

        while lower_cap <= upper_cap:
            middle_cap = (lower_cap + upper_cap) // 2

            running_day = 1
            to_fill = middle_cap
            for weight in weights:
                if weight > to_fill:
                    to_fill = middle_cap
                    running_day += 1
                to_fill -= weight
                   
            if running_day > days:
                lower_cap = middle_cap + 1
            else:
                upper_cap = middle_cap - 1
                min_cap = min(min_cap, middle_cap)
                
        return min_cap
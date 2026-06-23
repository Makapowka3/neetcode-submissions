class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0

        for i in range(len(tickets)):
            if i < k:
                time_taken += min(tickets[k], tickets[i])
            elif i > k:
                time_taken += min(tickets[k]-1, tickets[i])
            else:
                time_taken += tickets[k]

        return time_taken
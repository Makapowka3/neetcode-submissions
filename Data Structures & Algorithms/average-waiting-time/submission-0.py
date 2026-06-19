class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish, total = 0, 0

        for customer in customers:
            start = customer[0]
            if start >= finish:
                total += customer[1]
                finish = start + customer[1]
            else:
                total += (finish - start) + customer[1]
                finish += customer[1]
        
        return total / len(customers)

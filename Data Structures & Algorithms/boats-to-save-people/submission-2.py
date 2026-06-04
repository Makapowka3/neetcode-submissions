class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1, p2 = 0, len(people) - 1
        counter = 0
        while p1 <= p2:
            to_fill = limit
            people_l = 0
            for _ in range(2):
                if to_fill - people[p2] >= 0 and people_l < 2:
                    to_fill -= people[p2]
                    people_l += 1
                    p2 -= 1
            for _ in range(2):
                if to_fill - people[p1] >= 0 and people_l < 2:
                    to_fill -= people[p1]
                    people_l += 1
                    p1 += 1
            counter += 1

        return counter
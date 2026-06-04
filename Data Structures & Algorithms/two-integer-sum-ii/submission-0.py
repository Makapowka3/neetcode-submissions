class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                res.append(p1 + 1)
                res.append(p2 + 1)
                return res
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                p2 -= 1




        return res
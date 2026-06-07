class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashset = set(i for i in range(1, (len(grid)**2) + 1))
        for row in grid:
            for el in row:
                if el in hashset:
                    hashset.remove(el)
                else:
                    a = el
        return [a, hashset.pop()]
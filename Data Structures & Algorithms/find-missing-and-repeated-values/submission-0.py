class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashset = set(i for i in range(1, len(grid)**2 + 1))
        for row in grid:
            for v in row:
                if v not in hashset:
                    a = v
                else:
                    hashset.remove(v)
        b = hashset.pop()
        return [a,b]
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hashset = set(range(1,n*n + 1))
        for row in grid:
            for v in row:
                if v not in hashset:
                    a = v
                else:
                    hashset.remove(v)
        b = hashset.pop()
        return [a,b]
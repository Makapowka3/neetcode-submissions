class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = 0, float('inf')
        hash1 = Counter(s)

        for v in hash1.values():
            if v % 2 == 0:
                minEven = min(minEven, v)
            else:
                maxOdd = max(maxOdd, v)
        
        return maxOdd - minEven
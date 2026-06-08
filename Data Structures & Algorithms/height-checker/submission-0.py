class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        initial = heights.copy()
        heights.sort()
        
        res = 0
        for i in range(len(heights)):
            if initial[i] != heights[i]:
                res += 1
        
        return res
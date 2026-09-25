class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []

        curr_max = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > curr_max:
                res.append(i)
            curr_max = max(curr_max, heights[i])
        
        res.reverse()
        return res
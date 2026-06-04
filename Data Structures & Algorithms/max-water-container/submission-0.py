class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        in_len = (p2 - p1) * min(heights[p1],heights[p2])
        while p1 < p2:
            if heights[p1] < heights[p2]:
                p1 += 1
                print('y')
            else:
                p2 -= 1
                print('l')
            in_len = max(in_len, (p2 - p1) * min(heights[p1],heights[p2]))
            print(in_len)
        return in_len


        
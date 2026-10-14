class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial = image[sr][sc]
        if initial == color: return image
        image[sr][sc] = color
        def go(sr, sc, color):
            changed = True
            while changed:
                changed = False
                if sr >= 0 and sr+1 < len(image) and image[sr+1][sc] == initial:
                    changed = True
                    image[sr+1][sc] = color
                    go(sr+1, sc, color)
                elif sr-1 >= 0 and sr < len(image) and image[sr-1][sc] == initial:
                    changed = True
                    image[sr-1][sc] = color
                    go(sr-1, sc, color)
                elif sc >= 0 and sc+1 < len(image[0]) and image[sr][sc+1] == initial:
                    changed = True
                    image[sr][sc+1] = color
                    go(sr, sc+1, color)
                elif sc-1 >= 0 and sc < len(image[0]) and image[sr][sc-1] == initial:
                    changed = True
                    image[sr][sc-1] = color
                    go(sr, sc-1, color)

        go(sr,sc,color)
        return image
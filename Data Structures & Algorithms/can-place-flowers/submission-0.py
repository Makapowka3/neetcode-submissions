class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) <= 2:
            c = 0
            for flower in flowerbed:
                if flower == 1:
                    c += 1
            if n != 0 and c != 0:
                return False
            return True

        counter = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            counter += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            counter += 1
            flowerbed[-1] = 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    counter += 1
                    flowerbed[i] = 1
        if counter >= n:
            return True
        return False
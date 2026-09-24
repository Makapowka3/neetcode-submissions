class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            smallest = heapq.heappop(gifts)
            smallest = int(abs(smallest) ** 0.5)
            heapq.heappush(gifts, -smallest)
        
        return -sum(gifts)
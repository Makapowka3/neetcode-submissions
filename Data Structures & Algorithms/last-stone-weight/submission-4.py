class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones[:]
        heapq.heapify_max(heap)
        while len(heap) > 1:
            s1 = heapq.heappop_max(heap)
            s2 = heapq.heappop_max(heap)
            if s1 == s2:
                continue
            else:
                heapq.heappush_max(heap, abs(s1-s2))
        if heap:
            return heap[0]
        return 0
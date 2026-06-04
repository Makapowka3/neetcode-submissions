class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s1 == s2:
                continue
            else:
                heapq.heappush(heap, -(abs(s1-s2)))
        if heap:
            return abs(heap[0])
        return 0
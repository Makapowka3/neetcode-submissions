class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(arr)
        for i in range(k):
            n, i = heapq.heappop(arr)
            nums[i] *= multiplier
            heapq.heappush(arr, (nums[i], i))
        
        return nums
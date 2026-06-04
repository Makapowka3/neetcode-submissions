class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_v = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_v
            max_v = max(max_v, temp)
        return arr
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        max_v = arr[-1]
        
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_v
            max_v = max(max_v, temp)
        arr[-1] = -1
        return arr
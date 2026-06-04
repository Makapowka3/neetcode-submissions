class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        arr.reverse()
        max_v = arr[0]
        
        for i in range(1, len(arr)):
            temp = arr[i]
            arr[i] = max_v
            max_v = max(max_v, temp)
        arr[0] = -1
        arr.reverse()
        return arr
            
            
            
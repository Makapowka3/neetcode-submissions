class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        max_el = arr[0]
        arr[0] = -1
        for i in range(1, len(arr)):
            temp = arr[i]
            arr[i] = max_el
            if temp > max_el:
                max_el = temp
        arr.reverse()
        return arr
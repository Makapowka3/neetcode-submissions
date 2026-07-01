class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        run_max = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = run_max
            run_max = max(temp, run_max)
        
        return arr
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr) 
        
        lower, upper = 0, len(arr) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if d == 0:
                return arr[0]
            else:
                if arr[middle] == arr[0] + middle * d:
                    lower = middle + 1
                else:
                    upper = middle - 1
        return int((arr[lower] + arr[upper]) / 2)
            
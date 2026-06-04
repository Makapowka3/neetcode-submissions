class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[1] - arr[0] == arr[2] - arr[1]: d = arr[1] - arr[0]
        else: d = ((arr[1] - arr[0]) + (arr[2] - arr[1])) / 3
        
        lower, upper = 0, len(arr) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if d < 0:
                if arr[middle] == arr[0] + middle * d:
                    lower = middle + 1
                else:
                    upper = middle - 1
            elif d > 0:
                if arr[middle] == arr[0] + middle * d:
                    lower = middle + 1
                else:
                    upper = middle - 1
            else:
                return arr[0]
        return int((arr[lower] + arr[upper]) / 2)
            
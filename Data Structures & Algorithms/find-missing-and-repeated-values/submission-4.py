class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n

        expected_sum = N * (N + 1) // 2
        expected_square_sum = N * (N + 1) * (2 * N + 1) // 6

        actual_sum = 0
        actual_square_sum = 0

        for row in grid:
            for x in row:
                actual_sum += x
                actual_square_sum += x * x

        diff = actual_sum - expected_sum
        # diff = repeated - missing

        square_diff = actual_square_sum - expected_square_sum
        # square_diff = repeated^2 - missing^2
        # square_diff = (repeated - missing)(repeated + missing)

        sum_repeated_missing = square_diff // diff
        # sum_repeated_missing = repeated + missing

        repeated = (diff + sum_repeated_missing) // 2
        missing = sum_repeated_missing - repeated

        return [repeated, missing]
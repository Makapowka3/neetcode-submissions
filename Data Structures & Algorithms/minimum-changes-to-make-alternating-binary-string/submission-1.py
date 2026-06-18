class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0

        for i in range(len(s)):
            expected = str(i % 2)  # pattern 010101...
            if s[i] != expected:
                changes += 1

        return min(changes, len(s) - changes)
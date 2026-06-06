class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        running_prefix = shortest
        for i in range(len(strs)):
            for j in range(len(shortest)):
                if strs[i][j] != shortest[j]:
                    running_prefix = running_prefix[:j]
        return running_prefix
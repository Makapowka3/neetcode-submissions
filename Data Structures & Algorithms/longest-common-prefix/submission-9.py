class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)

        res = ''
        for i in range(len(prefix)):
            for j in range(len(strs)):
                if strs[j][i] != prefix[i]:
                    return res
            res += prefix[i]

        return res
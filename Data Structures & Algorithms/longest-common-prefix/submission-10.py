class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs, key=len)
        for w in strs:
            for i in range(len(word)):
                if word[i] != w[i]:
                    word = w[:i]
                    break
        return word
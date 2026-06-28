class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if dp[i]:
                for word in wordDict:
                    if s.startswith(word, i):
                        dp[i + len(word)] = True

        return dp[n]
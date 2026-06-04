class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        for s in strs:
            running = ""
            for ch in s:
                running += ch
                if running in hashmap:
                    hashmap[running] += 1
                else:
                    hashmap[running] = 1
        longest = ''
        for k, v in hashmap.items():
            if v == len(strs):
                if len(k) >= len(longest):
                    longest = k
        return longest
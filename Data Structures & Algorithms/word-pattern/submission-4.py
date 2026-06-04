class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        hashmap = {}
        seen = set()
        p1, p2 = 0, 0
        while p1 < len(pattern) and p2 < len(s):
            if pattern[p1] not in hashmap:
                if s[p2] in seen:
                    return False
                hashmap[pattern[p1]] = s[p2]
                seen.add(s[p2])
            else:
                if hashmap[pattern[p1]] != s[p2]:
                    return False
            p1 += 1
            p2 += 1
        return True
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        pref = [0]
        for el in code:
            pref.append(pref[-1] + el)

        res = []

        for i in range(n):
            if k > 0:
                end = i + k

                if end < n:
                    total = pref[end + 1] - pref[i + 1]
                else:
                    # From i+1 to the end, then from index 0
                    total = pref[n] - pref[i + 1]
                    total += pref[end % n + 1]

            else:
                start = i + k

                if start >= 0:
                    total = pref[i] - pref[start]
                else:
                    # From index 0 to i-1, plus the wrapped tail
                    total = pref[i]
                    total += pref[n] - pref[start % n]

            res.append(total)

        return res
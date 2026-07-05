class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash1 = Counter(arr)

        for key, v in hash1.items():
            if v == 1:
                if k == 1:
                    return key
                else:
                    k -= 1

        return ''
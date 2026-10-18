class Solution:
    def reverseBits(self, n: int) -> int:
        list_n = list(f"{n:032b}")
        res = 0

        for i in range(len(list_n)):
            res += (int(list_n[i]) * (2**i))

        return res
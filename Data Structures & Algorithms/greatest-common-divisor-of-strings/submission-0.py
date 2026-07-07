class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(n, m):
            res = 1
            for i in range(1, min(n, m)+1):
                if n % i == 0 and m % i == 0:
                    res = i
            return res

        if str1 + str2 != str2 + str1:
            return ''
        
        g = gcd(len(str1), len(str2))
        print(g)
        return str1[:g]
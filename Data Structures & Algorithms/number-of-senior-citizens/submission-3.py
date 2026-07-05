class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for det in details:
            if int(det[11:13]) > 60:
                res += 1
        return res
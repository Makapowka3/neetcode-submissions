class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for info in details:
            if int(info[11] + info[12]) > 60:
                counter += 1
        return counter
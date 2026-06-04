class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        real_digits = 0
        for i, v in enumerate(digits):
            real_digits += v * (10**(len(digits) - i- 1))
        real_digits += 1
        new_list = []
        for ch in str(real_digits):
            new_list.append(int(ch))
        return new_list
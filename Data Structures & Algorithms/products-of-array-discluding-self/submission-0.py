class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []

        zero_c = 0
        for el in nums:
            if el == 0:
                zero_c += 1
        
        total_mult = 1
        for el in nums:
            if el != 0:
                total_mult *= el
        
        for el in nums:
            if zero_c > 1:
                new_list.append(0)
                continue
            
            if zero_c == 1 and el != 0:
                new_list.append(0)
            elif zero_c == 1 and el == 0:
                new_list.append(total_mult)
            
            else:
                new_list.append(int(total_mult / el))
        
        return new_list
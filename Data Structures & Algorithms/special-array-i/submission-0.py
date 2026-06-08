class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        arr_type = -1
        if nums[0] % 2 == 0:
            arr_type = 1
        else:
            arr_type = 2

        if arr_type == 1:
            for i in range(1, len(nums)):
                if i % 2 == 0:
                    if nums[i] % 2 != 0:
                        return False
                else:
                    if nums[i] % 2 != 1:
                        return False
        else:
            for i in range(1, len(nums)):
                if i % 2 == 0:
                    if nums[i] % 2 != 1:
                        return False
                else:
                    if nums[i] % 2 != 0:
                        return False
        return True

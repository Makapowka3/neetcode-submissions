class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot_id = [0, None]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot_id[0] += 1
                pivot_id[1] = i

        if pivot_id[0] > 1:
            return False
        elif pivot_id[0] == 0:
            return True
        
        else:
            for i in range(0, pivot_id[1]):
                if nums[i] < nums[i-1]:
                    return False
        return True
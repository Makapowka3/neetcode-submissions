class Solution:
    def check(self, nums: List[int]) -> bool:
        drop = []
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                drop.append(i)
                if len(drop) == 2:
                    return False
        
        return True

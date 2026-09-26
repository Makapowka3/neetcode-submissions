class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #removing negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        res = 1
        curr = 0
        pos_flag = True
        next_v = True

        while pos_flag and next_v:
            curr = 0
            pos_flag = False
            next_v = False
            while curr < len(nums):
                if nums[curr] > 0:
                    pos_flag = True
                if nums[curr] == res:
                    next_v = True
                    res += 1
                    nums[curr] = -nums[curr]
                curr += 1
        
        return res

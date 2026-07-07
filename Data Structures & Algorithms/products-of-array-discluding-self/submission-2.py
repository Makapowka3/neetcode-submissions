class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_l = [1,]
        prefix_r = [1,]
        for i in range(len(nums)):
            prefix_l.append(prefix_l[i]*nums[i])
            prefix_r.append(prefix_r[i]*nums[len(nums)-i-1])
        
        res = []
        for i in range(len(nums)):
            res.append(prefix_l[i] * prefix_r[len(nums)-i-1])
        
        return res
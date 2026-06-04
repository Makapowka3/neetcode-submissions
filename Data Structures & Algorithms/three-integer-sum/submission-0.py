class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def two_sum(num, target):
            seen = {}
            duplets = []
            for i in range(len(num)):
                v = target - num[i]
                if v in seen:
                    duplets.append([v, num[i]])
                seen[num[i]] = True
            return duplets
        for i in range(len(nums)):
            comps = two_sum(nums[:i]+nums[i+1:], 0 - nums[i])
            for el in comps:
                trip = tuple(sorted([nums[i]]+el))
                res.add(trip)
        return list(res)
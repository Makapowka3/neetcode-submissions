class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                l, r = j + 1, n - 1
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
        return res
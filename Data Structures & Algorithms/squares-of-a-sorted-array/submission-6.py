class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        drop = 0 if nums[0] >= 0 else len(nums)
        for i in range(1, len(nums)):
            if nums[i] >= 0 and nums[i-1] < 0:
                drop = i

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        p1, p2 = drop-1, drop
        while p1 > -1 and p2 < len(nums):
            if nums[p1] < nums[p2]:
                output.append(nums[p1])
                p1 -= 1
            else:
                output.append(nums[p2])
                p2 += 1

        while p1 > -1:
            output.append(nums[p1])
            p1 -= 1
        while p2 < len(nums):
            output.append(nums[p2])
            p2 += 1
        
        for i in range(len(output)):
            output[i] = (output[i]**2)
        
        return output
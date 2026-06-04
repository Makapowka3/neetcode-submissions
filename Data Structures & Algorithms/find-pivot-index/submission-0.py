class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0,]
        right_sum = [0,]

        for i in range(1, len(nums)+1):
            left_sum.append(left_sum[i-1] + nums[i-1])
        
        nums.reverse()
        for i in range(1, len(nums)+1):
            right_sum.append(right_sum[i-1] + nums[i-1])
        right_sum.reverse()
        print(left_sum, right_sum)
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i+1]:
                return i
        
        return -1


        
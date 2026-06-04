class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []

        result_array_left = len(nums) * [None]
        result_array_right = len(nums) * [None]

        i = 0
        for el in nums:
            if i == 0:
                result_array_left[0] = 1
            elif i == 1:
                result_array_left[1] = nums[0]
            else:
                result_array_left[i] = result_array_left[i-1] * nums[i-1]
            i += 1
        
        nums_copy = nums.copy()
        invert_nums = []
        for _ in range(len(nums_copy)):
            invert_nums.append(nums_copy.pop())
        
        j = 0
        for el in invert_nums:
            if j == 0:
                result_array_right[0] = 1
            elif j == 1:
                result_array_right[1] = invert_nums[0]
            else:
                result_array_right[j] = result_array_right[j-1] * invert_nums[j-1]
            j += 1

        t = 0
        for el in nums:
            new_list.append(result_array_left[t]*result_array_right[len(nums)-t-1])
            t += 1
        print(result_array_left)
        print(result_array_right)
        return new_list

        

        
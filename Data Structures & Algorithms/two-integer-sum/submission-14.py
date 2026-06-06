class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        el_dict = {}
        for i in range(len(nums)):
            if nums[i] in el_dict:
                el_dict[nums[i]].append(i)
            else:
                el_dict[nums[i]] = [i,]
        for i in range(len(nums)):
            if target - nums[i] in el_dict:
                if len(el_dict[target-nums[i]]) == 1:
                    if target - nums[i] != nums[i]:
                        return [i, el_dict[target-nums[i]][0]]
                    else:
                        continue
                else:
                    return el_dict[target-nums[i]]


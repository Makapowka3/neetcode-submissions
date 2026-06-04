class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for ch in nums:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        for v in dict1:
            negr = target - v
            dict1[v] -= 1
            if negr in dict1 and dict1[negr] > 0:
                counter1 = 0
                counter2 = 0
                for n in nums:
                    if n == v:
                        nums.remove(v)
                        break
                    elif n != v:
                        counter1 += 1
                for n in nums:
                    if n == negr:
                        break
                    elif n != negr:
                        counter2 += 1
                return [counter1, counter2 + 1]


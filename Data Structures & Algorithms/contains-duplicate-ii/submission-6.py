class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 or k < 1:
            return False
        hashmap = set()
        p1 = 0
        p2 = 0
        while p2 != k+1 and p2 < len(nums):
            if nums[p2] not in hashmap:
                hashmap.add(nums[p2])
            else:
                return True
            p2 += 1
        
        while p2 < len(nums):
            hashmap.remove(nums[p1])
            if nums[p2] in hashmap:
                return True
            hashmap.add(nums[p2])
            p1 += 1
            p2 += 1

        return False
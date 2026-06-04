class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        for ch in arr:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
        
        counter = 1
        for ch in arr:
            if hashmap[ch] == 1:
                if counter == k:
                    return ch
                counter += 1
                    
        return ''
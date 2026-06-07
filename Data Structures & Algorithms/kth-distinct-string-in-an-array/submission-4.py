class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = defaultdict(int)

        for el in arr:
            hashmap[el] += 1
        
        counter = 1
        for el in hashmap:
            if hashmap[el] == 1:
                if counter == k:
                    return el
                counter += 1
                
        return ''
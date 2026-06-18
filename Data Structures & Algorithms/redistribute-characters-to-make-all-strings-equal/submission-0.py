class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = defaultdict(int)

        for word in words:
            for letter in word:
                hashmap[letter] += 1
        
        for letter in hashmap:
            if hashmap[letter] % len(words) != 0:
                return False
        
        return True
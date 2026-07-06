class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i in range(len(order)):
            hashmap[order[i]] = i
        
        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if j == len(words[i]):
                    return False

                if words[i-1][j] != words[i][j]:
                    if hashmap[words[i-1][j]] > hashmap[words[i][j]]:
                        return False
                    break
        
        return True
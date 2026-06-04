class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        len_count = 0
        i, j = 0, 0
        
        while j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num
            
            else:
                if i >= n or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == n
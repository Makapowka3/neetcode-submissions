class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p_word = 0
        p_abbr = 0
        expected_len = 0

        while p_abbr < len(abbr) and p_word < len(word):
            if abbr[p_abbr].isdigit():
                if abbr[p_abbr] == '0':
                    return False
                
                num = 0
                while p_abbr < len(abbr) and abbr[p_abbr].isdigit():
                    num = num * 10 + int(abbr[p_abbr])
                    p_abbr += 1
                expected_len += num

                for _ in range(num):
                    p_word += 1
            
            else:
                if abbr[p_abbr] != word[p_word]:
                    return False
                    
                expected_len += 1

                p_abbr += 1
                p_word += 1

        return p_word == len(word) and p_abbr == len(abbr)
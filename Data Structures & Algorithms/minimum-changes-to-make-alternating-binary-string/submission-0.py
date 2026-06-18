class Solution:
    def minOperations(self, s: str) -> int:
        #count odd and even alternating and return the minimum

        odd_changes, even_changes = 0, 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    even_changes += 1
            else:
                if s[i] == '0':
                    even_changes += 1
        
        for i in range(len(s)):
            if i % 2 == 1:
                if s[i] == '1':
                    odd_changes += 1
            else:
                if s[i] == '0':
                    odd_changes += 1
        
        return min(odd_changes, even_changes)
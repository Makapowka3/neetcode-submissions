class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split('@')
            current = []
            for ch in local:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                else:
                    current.append(ch)
            
            current.append(domain)
            unique.add(''.join(current))
        
        return len(unique)
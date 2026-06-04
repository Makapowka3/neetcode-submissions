class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for mail in emails:
            cleaned = []
            local, domain = mail.split('@')
            for ch in local:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                else:
                    cleaned.append(ch)
            normalized = ''.join(cleaned) + '@' + domain
            if normalized not in hashset:
                hashset.add(normalized)
        return len(hashset)

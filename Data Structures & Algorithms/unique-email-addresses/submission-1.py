class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        diff = 0
        hashset = set()
        for mail in emails:
            res = ''
            local, domain = mail.split('@')
            for ch in local:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                else:
                    res += ch
            res += '@' + domain
            if res not in hashset:
                hashset.add(res)
                diff += 1
        return diff

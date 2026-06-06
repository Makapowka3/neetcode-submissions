class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for em in emails:
            local, domain = em.split('@')
            email = []
            for el in local:
                if el == '+':
                    break
                elif el != '.':
                    email.append(el)
            email.append(domain)
            unique.add(''.join(email))

        return len(unique)

                    
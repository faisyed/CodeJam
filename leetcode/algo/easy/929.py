class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split('@')
            if "+" in local:
                local_lis = local.split("+")
                local = local_lis[0]
            if "." in local:
                local = "".join(local.split("."))
            res.add(local+"@"+domain)
        return len(res)
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        
        for e in emails:
            # 1. Split by domain
            local, domain = e.split('@', 1)
            # 2. Check/Split for ignored parts - only local_parts[0] is relevant
            local_parts = local.split('+', 1)            
            # 3. Remove periods
            # clean_local = ''.join(local_parts[0].split('.'))
            clean_local = local_parts[0].replace('.', '')
            
            st.add(f'{clean_local}@{domain}')
        
        # print(st)
        return len(st)
            

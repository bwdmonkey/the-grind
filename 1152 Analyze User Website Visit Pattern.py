# https://leetcode.com/problems/analyze-user-website-visit-pattern/

from itertools import combinations
from collections import defaultdict, Counter

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 1. sort by time
        tuples = sorted(zip(timestamp, username, website))
        
        # 2. group by user
        sites_by_user = defaultdict(list)
        for time, user, site in tuples:
            sites_by_user[user].append(site)
            
        # 3. group into 3 seqs
        three_seqs = Counter()
        for user, sites in sites_by_user.items():
            if len(sites) >= 3:
                # get set of combinations to avoid duplicate three_seq
                for three_seq in set(combinations(sites, r=3)):
                    three_seqs[three_seq] += 1

        # print(three_seqs)
        res = min(three_seqs.items(), key=lambda e: (-e[1], e[0]))
        return res[0]
        
        
        
        

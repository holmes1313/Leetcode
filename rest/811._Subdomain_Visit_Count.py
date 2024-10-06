# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:40:35 2019

@author: z.chen7
"""

# 811. Subdomain Visit Count
"""
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""
from collections import Counter

def subdomainVisits(cpdomains):
    """
    :type subdomainVisits: List[str]
    :rtype: List[str]
    """
    
    """
    self solution
    
    result = []
    domain_visit = {}
    for domain in cpdomins:
        visit_amount = int(domain.split(" ")[0])
        dot_amount = domain.split(" ")[1]
        for i in range(dot_amount.count(".")+1):
            domin_name = domain.split(" ")[1].split(".", i)[-1]
            if domin_name in domain_visit.keys():
                domain_visit[domin_name] += visit_amount
            else:
                domain_visit[domin_name] = visit_amount
    
    for domain, visit in domain_visit.items():
        result.append(str(visit) + " " + domain)
        
    return result
    """
    
    # Best answer
    # 1 collection.Counter
    # 2 ".".join(frags[i:])
    # 3 "{} {}".format(count, domain)
    domain_visit =  Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split(".")
        for i in range(len(frags)):
            domain_visit[".".join(frags[i:])] += count
            
        return ["{} {}".format(count, domain) for domain, count in domain_visit.items()]
    
    
    
    
    

domain = "9001 discuss.leetcode.com"
count, domain = domain.split()
count
domain
count  = int(count)
frags = domain.split(".")
frags
for i in range(len(frags)):
    print(".".join(frags[i:]))


subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])

aa = [1]
aa.append(2)
aa
aa = "9001 discuss.leetcode.com"
aa.count(".")
visit = aa.split(" ")[0]
aa.split(" ")[1].split(".", 2)
aa[0].split(".", 1)

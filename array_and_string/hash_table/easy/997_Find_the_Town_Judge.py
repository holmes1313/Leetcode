"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

"""
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1

        trusted = {}
        trusting = {}
        for rel in trust:
            if rel[0] not in trusting:
                trusting[rel[0]] = 1
            else:
                trusting[rel[0]] += 1

            if rel[1] not in trusted:
                trusted[rel[1]] = 1
            else:
                trusted[rel[1]] += 1

        for id, vote in trusted.items():
            if vote == n - 1 and id not in trusting:
                return id

        return -1


class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        mapping = {}
        for t1, t2 in trust:
            if t1 not in mapping:
                mapping[t1] = [1, 0]
            else:
                mapping[t1][0] += 1
            if t2 not in mapping:
                mapping[t2] = [0, 1]
            else:
                mapping[t2][1] += 1

        for key, value in mapping.items():
            if value[0] == 0 and value[1] == n -1:
                return key

        return -1
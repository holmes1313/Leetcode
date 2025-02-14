"""
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.

 

Example 1:

Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
 

Constraints:

1 <= playerId, K <= 10000
It's guaranteed that K is less than or equal to the current number of players.
1 <= score <= 100
There will be at most 1000 function calls.
"""
class Leaderboard1(object):

    def __init__(self):
        self.id_to_score = {}
        
    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.id_to_score:
            self.id_to_score[playerId] = score
        else:
            self.id_to_score[playerId] += score
        
    def top2(self, K):
        """
        :type K: int
        :rtype: int
        """
        top_k_players = sorted(self.id_to_score.keys(), key=lambda x: self.id_to_score[x], reverse=True)[:K]
        ans = 0
        for p in top_k_players:
            ans += self.id_to_score[p]
        return ans

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        min_heap = []
        for p, score in self.id_to_score.items():
            heapq.heappush(min_heap, (score, p))
            if len(min_heap) > K:
                heapq.heappop(min_heap)
        res = 0
        while min_heap:
            score, player = heapq.heappop(min_heap)
            res += score
        return res

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.id_to_score[playerId] = 0
        
class Leaderboard(object):

    def __init__(self):
        self.id_to_score = {}
        # Initialize sorted_scores called sorted_scores. 
        # The underlying data structure for SortedList is a balanced tree structure.
        # O(logn) - search/add/remove operations
        from sortedcontainers import SortedList
        self.sorted_scores = SortedList()
        
    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.id_to_score:
            self.id_to_score[playerId] = score
            self.sorted_scores.add((-score, playerId))
        else:
            old_score = self.id_to_score[playerId]
            self.sorted_scores.remove((-old_score, playerId))
            new_score = old_score + score
            self.id_to_score[playerId] = new_score
            self.sorted_scores.add((-new_score, playerId))

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        top_k_total = 0
        for score, pid in self.sorted_scores[:K]:
            top_k_total += -score
        return top_k_total

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        old_score = self.id_to_score[playerId]
        self.sorted_scores.remove((-old_score, playerId))
        del self.id_to_score[playerId]

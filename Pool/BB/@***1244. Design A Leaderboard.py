"""
Top K traded stocks by volume

用两个数据结构：
HashMap<Stock>快速访问
TreeSet<Stock>来维持sorted

execute_trade(company, volume)
print_topk_company(top_n)
举例:
execute_trade("MSFT", 900)
execute_trade("APPL", 300)
execute_trade("GOOG", 1000)
execute_trade("APPL", 400)
execute_trade("META", 200)
execute_trade("BA", 500)
print_topk_company(2):
  GOOG|1000, MSFT|900, APPL|700,
让print_topk_company越快越好
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
        



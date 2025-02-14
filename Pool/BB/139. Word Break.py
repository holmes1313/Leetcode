class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        # dp[i] indicates whether the substring s[0:i] can be segmented into words from the dictionary.
        dp = [False] * (n+1)
        # Base case: empty string can be segmented
        dp[0] = True
        word_set = set(wordDict)
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
        return dp[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word and dp[i]:
                    dp[i+len(word)] = True 
        return dp[-1]


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        queue = collections.deque([0])
        seen = set([0])
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start, len(s)+1):
                if end in seen:
                    continue
                
                sub_str = s[start: end]
                if sub_str in word_set:
                    seen.add(end)
                    queue.append(end)
        return False


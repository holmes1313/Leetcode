"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

"""
import collections
import heapq


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        max_freq = max(count.values())
        if max_freq > (len(s)+1) // 2:
            return ""

        max_heap = []
        for cha, freq in count.items():
            heapq.heappush(max_heap, (-freq, cha))

        result = []
        prev_freq, prev_cha = 0, ""
        while max_heap:
            freq, cha = heapq.heappop(max_heap)
            result.append(cha)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_cha))

            prev_freq = freq + 1
            prev_cha = cha

        return "".join(result)

    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = collections.Counter(s)

        if max(counts.values()) > (len(s)+1)//2:
            return ""

        max_heap = []
        for val, count in counts.items():
            heapq.heappush(max_heap, (-count, val))

        new_string = []
        prev_count, prev_val = 0, ""
        cooling_queue = collections.deque()
        position = 0
        while max_heap or cooling_queue:
            position += 1
            if max_heap:            
                freq, cha = heapq.heappop(max_heap)
                new_string.append(cha)

                freq += 1
                if freq < 0:
                    cooling_queue.append((freq, cha, position+1))

            if cooling_queue:
                if cooling_queue[0][2] <= position:
                    freq, cha, _ = cooling_queue.popleft()
                    heapq.heappush(max_heap, (freq, cha))

        return "".join(new_string)

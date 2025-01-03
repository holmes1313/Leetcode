"""
You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

 

Example 1:

Input: s = "EEEEEEE"

Output: 7

Explanation:

After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

Example 2:

Input: s = "ELELEEL"

Output: 2

Explanation:

Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second.


Constraints:

1 <= s.length <= 50
s consists only of the letters 'E' and 'L'.
s represents a valid sequence of entries and exits.

"""
class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_count = 0
        for cha in s:
            if cha == "E":
                stack.append(cha)
            else:
                stack.pop()

            max_count = max(max_count, len(stack))

        return max_count
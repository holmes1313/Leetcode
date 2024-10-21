"""
You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.


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
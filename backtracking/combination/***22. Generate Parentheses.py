"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
import collections


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                result.append(path)
                return

            # Add an opening parenthesis if the count of opening parentheses is less than n.
            if open_count < n:
                backtrack(path + "(", open_count+1, close_count)

            # Add a closing parenthesis if the count of closing parentheses is less than the count of opening parentheses.
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count+1)

        result = []
        backtrack("", 0, 0)
        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def is_valid(p_str):
            open_count = 0

            for cha in p_str:
                if cha == "(":
                    open_count += 1
                else:
                    open_count -= 1

                if open_count < 0:
                    return False

            return open_count == 0


        ans = []
        queue = collections.deque([""])
        while queue:
            p_str = queue.pop()

            if len(p_str) == 2*n:
                if is_valid(p_str):
                    ans.append(p_str)

                continue

            queue.append(p_str + "(")
            queue.append(p_str + ")")

        return ans


        
"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:



Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
Example 2:



Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

"""

class Solution(object):
    def minOperations1(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        is_main = True
        depth = 0
        for log in logs:
            is_main = (depth == 0)
            if log == "../":
                if not is_main:
                    depth -= 1
            elif log != "./":
                depth += 1

        return abs(depth)

    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []

        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()

            elif log != "./":
                stack.append(log)

        return len(stack)
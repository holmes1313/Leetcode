"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

"""
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = {(0, 0)}  # set of tuple (Immutable)
        x = y = 0
        for p in path:
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "W":
                x -= 1
            elif p == "E":
                x += 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False

        
"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(a):
                        break
                    elif stack[-1] < abs(a):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] > -a:
                    break
                elif stack[-1] == -a:
                    stack.pop()
                    break
                else:
                    stack.pop()
            else: # Code to execute if the while loop completes without a break
                stack.append(a)

        return stack
        
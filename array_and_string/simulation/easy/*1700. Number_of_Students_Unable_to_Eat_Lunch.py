"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
"""
import collections


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        queue = collections.deque(students)  # Convert the list of students into a queue
        sandwich_index = 0       # Index for the current sandwich on top of the stack
        n = len(sandwiches)      # Total number of sandwiches
        count = 0                # Count of students who can't eat

        while count < n and queue:
            # If the student at the front of the queue prefers the top sandwich
            if queue[0] == sandwiches[sandwich_index]:
                # The student takes the sandwich and leaves the queue
                queue.popleft()
                sandwich_index += 1  # Move to the next sandwich
                count = 0             # Reset count since a student took a sandwich
            else:
                # The student does not want the top sandwich
                queue.append(queue.popleft())
                count += 1           # Increment the count of students who didn't take a sandwich

        return len(queue)  # Return the number of students left in the queue


    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter = collections.Counter(students)
        for sand in sandwiches:
            if counter.get(sand, 0) > 0:
                counter[sand] -= 1
            else:
                return sum(counter.values())
        return sum(counter.values())
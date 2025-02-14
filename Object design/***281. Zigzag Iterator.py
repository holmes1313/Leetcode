"""

Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.
 

Example 1:

Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
Example 2:

Input: v1 = [1], v2 = []
Output: [1]
Example 3:

Input: v1 = [], v2 = [1]
Output: [1]
"""
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.queue = collections.deque()
        for vec_index, vector in enumerate(self.vectors):
            if len(vector) > 0:
                self.queue.append((vec_index, 0))

    def next(self):
        """
        :rtype: int
        """
        vec_index, elem_index = self.queue.popleft()
        if elem_index + 1 < len(self.vectors[vec_index]):
            self.queue.append((vec_index, elem_index+1))
        return self.vectors[vec_index][elem_index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
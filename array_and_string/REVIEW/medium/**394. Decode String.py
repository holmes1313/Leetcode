"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class DListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert_at_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_at_head(node)
        return node.val
        
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_at_head(node)
        else:
            node = DListNode(key, value)
            self.cache[key] = node
            self._insert_at_head(node)

            if len(self.cache) > self.capacity:
                last_node = self.tail.prev
                self._remove(last_node)
                del self.cache[last_node.val]
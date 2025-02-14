"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_value = {}
        self.queue = collections.deque()
 
    def get(self, key):
        if key not in self.key_to_value:
            return -1

        value = self.key_to_value[key]
        self.queue.remove(key)
        self.queue.append(key)
        return value
        
    def put(self, key, value):
        if key in self.key_to_value:
            self.key_to_value[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            self.key_to_value[key] = value
            self.queue.append(key)

            if len(self.queue) > self.capacity:
                key_to_remove = self.queue.popleft()
                del self.key_to_value[key_to_remove]

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val_to_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_node_to_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def get(self, key):
        if key not in self.val_to_node:
            return -1

        node = self.val_to_node[key]

        # delete node
        self.delete_node(node)

        # put node to the head.next
        self.move_node_to_head(node)
        
        return node.val

    def put(self, key, val):
        if key in self.val_to_node:
            node = self.val_to_node[key]
            node.val = val
            # delete node
            self.delete_node(node)
            # put node to the head.next
            self.move_node_to_head(node)
        else:
            node = Node(key, val)
            self.val_to_node[key] = node
            self.move_node_to_head(node)
            if len(self.val_to_node) > self.capacity:
                last_node = self.tail.prev
                self.delete_node(last_node)
                del self.val_to_node[last_node.key]




# Python 3
import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)  # Move to the end to mark it as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move to the end to mark it as recently used

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item (from the beginning)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
https://www.1point3acres.com/bbs/thread-644592-1-1.html


"""

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
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


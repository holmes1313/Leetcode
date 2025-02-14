
"""
https://www.1point3acres.com/bbs/thread-1097351-1-1.html
"""
import random


class RandomizedSet(object):

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False

        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False
        
        index = self.val_to_index[val]
        last_val = self.values[-1]

        self.val_to_index[last_val] = index
        self.values[index] = last_val
        
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        # When you pass this view object to random.choice(), Python will implicitly convert it to a list (which is an O(n))
        # return random.choice(self.val_map.keys())
        return random.choice(self.values)

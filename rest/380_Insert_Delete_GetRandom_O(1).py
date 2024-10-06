# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:21:13 2019

@author: z.chen7
"""
# 380. Insert Delete GetRandom O(1)
"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element
 must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""


# using hashtable to achieve O(1)
# random 
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.loc = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.loc:
            return False
        
        self.array.append(val)
        self.loc[val] = len(self.array) - 1
        return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.loc:
            return False
        
        idx = self.loc[val]       # get val index in list
        last = self.array[-1]   # get the last addition
        self.array[idx] = last    # overwrite val index with last addition
        self.loc[last] = idx      # update the last addition's index to it's new spot    
        self.array.pop()          # get rid of the last addition as it's now put at idx
        del self.loc[val]        # # get rid of val's record in self.loc
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # random.randint(0, len(self.array)-1)
        return random.choice(self.array)
    
    
a = [1, 2, 3, 4, 5]
random.choice(a)
random.randint(0, len(a)-1)



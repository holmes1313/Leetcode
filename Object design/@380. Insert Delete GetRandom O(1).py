"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
class RandomizedSet(object):

    def __init__(self):
        # Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.
        # Array List has indexes and could provide GetRandom in average constant time, though has problems with Delete
        self.val_to_index = {}
        self.values = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Dictionary lookups in Python takes constant time
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

        # Deleting a value at an arbitrary index takes linear time. 
        # The solution here is to always delete the last value:
        # Swap the element to delete with the last one.
        # Pop the last element out.
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
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
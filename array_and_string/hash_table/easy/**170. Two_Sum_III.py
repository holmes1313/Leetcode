"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
"""

class TwoSum(object):

    def __init__(self):
        self.num_counts = {}
        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number not in self.num_counts:
            self.num_counts[number] = 1
        else:
            self.num_counts[number] += 1
        
    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts.keys():
            diff = value - num
            if diff != num:
                if diff in self.num_counts:
                    return True
            else:
                if self.num_counts[num] > 1:
                    return True

        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""
class SmallestInfiniteSet(object):

    def __init__(self):
        self.min_heap = []  # to store the added back nums
        self.seen = set()   # to track nums in heap
        self.next_num = 1
        
    def popSmallest(self):
        """
        :rtype: int
        """
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.seen.remove(smallest)
        else:
            smallest = self.next_num
            self.next_num += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.next_num and num not in self.seen:
            heapq.heappush(self.min_heap, num)
            self.seen.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:37:51 2019

@author: z.chen7
"""

# 1047. Remove All Adjacent Duplicates In String
"""
Input: "abbaca"
Output: "ca"

Solution: Stack
Keep a res as a characters stack. Iterate characters of S one by one.
If the next character is same as the last character in res, pop the last character from res.
If the next character is different, we append it to the end of res.
"""


# 1052. Grumpy Bookstore Owner
# get largest sum of K consecutive elements in a list
def maxKSum(target_list, k):
    result = 0
    current_k = 0
    for i in range(len(target_list)):
        current_k += target_list[i]
        if i >= k:
            current_k -= target_list[i - k]
            
        result = max(result, current_k)
        
    return result
    

# 107_Binary_Tree_Level_Order_Traversal_II
# tree level question
# dfs and bfs
import collections
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = 0
        result = collections.defaultdict(list)
        queue = collections.deque([(root, level)])
        
        while queue:
            node, level = queue.pop()
            result[level].append(node.val)
            
            if node.left:
                queue.appendleft((node.left, level+1))
                
            if node.right:
                queue.appendleft((node.right, level+1))
                
        return [result[i] for i in range(len(result)-1, -1, -1)]

    
class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        hashtable = collections.defaultdict(list)
        level = 0
        self.dfs(root, level, hashtable)
        return [hashtable[i] for i in range(len(hashtable) - 1, -1, -1)]
    
    def dfs(self, node, level, hashtable):
        hashtable[level].append(node.val)
        if node.left:
            self.dfs(node.left, level+1, hashtable)
        if node.right:
            self.dfs(node.right, level+1, hashtable)
        


# 112_Path_Sum
# tree value question
# breath first search
class Solution_112(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """     
        if not root:
            return False
        result = []
        queue = collections.deque([(root, 0)])
        while queue:
            node, value = queue.pop()
            if not node.left and not node.right:
                result.append(value + node.val)
            if node.left:
                queue.appendleft((node.left, value + node.val))
            if node.right:
                queue.appendleft((node.right, value + node.val))
        return target in result

# depth first search
class Solution_112_2(object):
    def hasPathSum(self, root, target):
        if not root:
            return False
        result = []
        self.helper(root, 0, result)
        return target in result
    
    def helper(self, node, value, result):
        if not node.left and not node.right:
            result.append(value + node.val)
        if node.left:
            self.helper(node.left, value+node.val, result)    
        if node.right:
            self.helper(node.right, value+node.val, result)



# 110. Balanced Binary Tree
# recursion
class Solution_110(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, node):
        if not node:
            return 0
        
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        return max(left, right) + 1
    

# 1137. N-th Tribonacci Number
# how to set memo
def tribonacci2(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = tribonacci2(n-2) + tribonacci2(n-1)
    return memo[n]


# 11. Container With Most Water
class Solution_11(object):
    def maxArea(self, height):
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        area = self.calculateArea(left, right, height)
        while left < right:
            if height[left] > height[right]:
                right -= 1
                area = max(area, self.calculateArea(left, right, height))
            else:
                left += 1
                area = max(area, self.calculateArea(left, right, height))     
        return area
    def calculateArea(self, left, right, height):
        return (right - left) * min(height[left], height[right]) 
    
    
    
# 15. 3sum
class Solution_15(object):
    def threeSum(self, nums):
        if not nums:
            return []
        nums.sort()
        result = []
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for curr in range(len(nums)-2):
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue
            left = curr + 1
            right = len(nums) - 1
            while left < right:
                s = nums[curr] + nums[left] + nums[right]
                if s < 0:
                    left += 1   
                elif s > 0:
                    right -= 1   
                else:
                    result.append([nums[curr], nums[left], nums[right]])   
                    while left < right and nums[left] == nums[left+1]:
                        left += 1       
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1   
                    left += 1
                    right -= 1
        return result


# 160. Intersection of Two Linked Lists
class Solution_160(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB  
         # two pointers
        # if either pointer hits the end, switch head and continue the second traversal, 
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa  
    
    
# 198. House Robber
def rob_topDown(nums, memo={}):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n not in memo:
        memo[n] = max(rob_topDown(nums[:-2]) + nums[-1], rob_topDown(nums[:-1]))
    print(memo)
    return memo[n]

def rob_bottomUp(nums):
    if not nums:
        return 0
    a = 0
    b = nums[0]
    for i in range(1, len(nums)):
        b, a = max(a+nums[i], b), b
    return b


# 200. Number of Islands
class Solution_200(object):
    def numIslands(self, matrix):
        if not matrix:
            return 0
        rn = len(matrix)
        cn = len(matrix[0])
        num = 0
        for i in range(rn):
            for j in range(cn):
                if matrix[i][j] == '1':
                    num += 1
                    self.bfs(matrix, i, j, rn, cn)
        #print matrix
        return num    
    def bfs(self, matrix, i, j, rn, cn):
        queue = collections.deque()
        queue.appendleft((i, j))
        while queue:
            x, y = queue.pop()
            # checking current element
            if matrix[x][y] == '1':
                matrix[x][y] = '2'
                # appending other elements
                for m, n in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= m < rn and 0 <= n < cn:
                        queue.appendleft((m, n))
                        
                        
# 204. Count primes
# Sieve of Eratosthenes
def countPrimes(n):
    if n < 3:
        return 0
    primes = [1] * n
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(n**0.5)+1):
        if primes[i] == 1:
            primes[i*i::i] = [0] * len(primes[i*i::i])
    return sum(primes)


# 237. Delete Node in a Linked List
# consider head situation
"""
if head.val == node.val:
    head = head.next
"""


# 238. Product of Array Except Self
# left prod * right prod
class Solution_238(object):
    def productExceptSelf(self, nums):
        left = 1
        left_prod = []
        right = 1
        right_prod = []

        for i in range(len(nums)):
            left_prod.append(left)
            left *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            right_prod.append(right)
            right *= nums[i]
        
        for i in range(len(nums)):
            left_prod[i] *= right_prod[len(nums) - i -1]
            
        return left_prod         


# 276. Paint Fence
# dp bottom up
class Solution_276(object):    
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        diff = k * (k-1)
        for i in range(3, n+1):
            same, diff = diff, (same + diff) * (k-1)
        return same + diff
    

# 380. Insert Delete GetRandom O(1)
# random element from a list
import random
my_list = [1, 2, 3]
random_idx = random.randint(0, len(my_list)-1)
random_element = random.choice(my_list)

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


# 392. Is Subsequence
def isSubsequence(s, t):
    for chr in s:
        idx = s.find(chr)
        if idx == -1:
            return False
        t = t[idx+1:]
    return True



def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_hashtable = {}
        max_len = 0
        start = 0
        import pdb;pdb.set_trace()    
        for i, char in enumerate(s):
            if char in index_hashtable:
                max_len = max(max_len, i - start)
                # update start of string index to the next index
                start = max(index_hashtable[char] + 1, start)
                # start = index_hashtable[char] + 1 can't deal with 'abbac'
            index_hashtable[char] = i
        # return should consider the last non-repeated substring
        return max(max_len, len(s) - start)


# 435. Non-overlapping Intervals
# take one with smallest end, 
# remove all the bad ones overlapping it
def eraseOverlapIntervals(intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        result = [intervals[0]]
        for i in intervals[1:]:
            if i[0] >= result[-1][1]:
                result.append(i)
                
        return len(intervals) - len(result)


# 543. Diameter of Binary Tree
def maxDepth(node):
    if not node:
        return 0
    left = maxDepth(node.left)
    right = maxDepth(node.right)
    
    return max(left, right) + 1



# 54. Spiral Matrix
def spiralOrder(matrix):
    if not matrix:
        return []
    
    head = matrix.pop(0)
    
    if len(matrix) > 1:
        rest = spiralOrder(list(zip(*matrix))[::-1])
        
    elif len(matrix) == 1:
        rest = matrix[0][::-1]
    # when matrix [[1]]
    else:
        rest = []
        
    return list(head) + list(rest)


# 560. Subarray Sum Equals K
# subarry sum -> cumulative sum
def subarrySum(nums, k):
    cumusum_dict = collections.Counter()
    cumusum = 0
    cumusum_dict[cumusum] += 1
    result = 0
    for n in nums:
        cumusum += n
        if cumusum - k in cumusum_dict:
            result += cumusum_dict[cumusum - k]
        cumusum_dict[cumusum] += 1
    return result


# 567. Permutation in String
# word1 is a permutation of word2? collections.Counter(word1) == collections.Counter(word2) 
def checkInclusion(s1, s2):
        if len(s2) < len(s1):
            return False
        # sliding window
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2[:len(s1)])
        for index in range(len(s1), len(s2)):
            if count1 == count2:
                return True 
            count2[s2[index]] += 1
            count2[s2[index - len(s1)]] -= 1
            if count2[s2[index - len(s1)]] == 0:
                del count2[s2[index - len(s1)]]     
        return count1 == count2
    

# 21. Merge Two Sorted Lists
def mergeTwoLists(l1, l2):
    root = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return root.next


# 605. Can Place Flowers
# sliding window
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        origin = sum(flowerbed)        
        if len(flowerbed) <= 2:
            return n + origin <= 1                        
        if flowerbed[:2] == [0, 0]:
            flowerbed[0] = 1
        if flowerbed[-2:] == [0, 0]:
            flowerbed[-1] = 1
        count = collections.Counter(flowerbed[:3])
        for index in range(3, len(flowerbed)):
            if count[0] == 3:
                flowerbed[index - 2] = 1
                count[0] -= 1
                count[1] += 1
            count[flowerbed[index]] += 1
            count[flowerbed[index-3]] -= 1
        return sum(flowerbed) - origin >= n


# 665. Non-decreasing Array
# fix either the current value or the next value appropriately so that any future inversions can be detected correctly.
class Solution(object):
    def checkPossibility(self, nums):        
        count = 0
        for i in range(len(nums)-1):            
            if nums[i] > nums[i+1]:
                count += 1
                if i == 0:
                    nums[i] = nums[i+1]                    
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]                
                elif nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]                    
        return count <= 1


# 706. Design HashMap
class Node(object):
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap(object):
    def __init__(self):
        self.bucket_number = 10000
        self.array = [None] * self.bucket_number

    def put(self, key, val):
        newNode = Node(key, val)
        index = self.calculateHashValue(key)
        if self.array[index] == None:
            self.array[index] = newNode
        else:
            head = self.array[index]
            if head.pair[0] == key:
                head.pair = (key, val)
            else:
                curr = head
                while curr and curr.next:
                    if curr.next.pair[0] == key:
                        curr.next.pair = (key, val)
                        return
                    curr = curr.next
                curr.next = newNode

    def get(self, key):
        index = self.calculateHashValue(key)
        head = self.array[index]
        curr = head
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1

    def remove(self, key):
        index = self.calculateHashValue(key)
        head = self.array[index]
        curr = head
        if head and head.pair[0] == key:
            self.array[index] = head.next
            return
        while curr and curr.next:
            if curr.next.pair[0] == key:
                curr.next = curr.next.next
            curr = curr.next

    def calculateHashValue(self, key):
        return key % self.bucket_number


# 724. Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)
        
        for index, num in enumerate(nums):
            left += num
            if left == right:
                return index
            right -= num        
        return -1


# 79. Word Search
# DFS!!
class Solution_79(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rn = len(board)
        cn = len(board[0])
        
        for i in range(rn):
            for j in range(cn):
                 if self.dfs(board, word, i, j):
                    return True
        return False        
   
    # check whether can find word, start at (i,j) position 
    def dfs(self, board, word, i, j):
        if len(word) == 0:  # all the characters are checked
                return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        temp = board[i][j]   # marked as visited for situation like board = [['a', 'a']], word = 'aaa'
        board[i][j] = '_'
        result = self.dfs(board, word[1:], i-1, j) or self.dfs(board, word[1:], i+1, j) or self.dfs(board, word[1:], i, j-1) or self.dfs(board, word[1:], i, j+1)
        board[i][j] = temp
        return result
    
    
# 78. Subsets
class Solution_78(object):
    def subsets(self, nums):
        result = []
        start = 0
        current = []
        self.backtrack(nums, start, current, result)
        return result
    
    def backtrack(self, nums, start, current, result):
        result.append(current[:])    # make copy of current
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.backtrack(nums, i+1, current, result)   # i + 1 instead of start + 1
            current.pop()
            
            
# 90. Subsets II  (contains duplicates)
class Solution_90(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        start = 0
        current = []
        nums.sort()   # unify [2, 1] to [1, 2] to skip duplicate
        self.backtrack(nums, start, current, result)
        return result
    
    def backtrack(self, nums, start, current, result):
        if current not in result:
            result.append(current[:])
        for i in range(start, len(nums)):
            # better way to skip duplicate
            #if i > start and nums[i] == nums[i-1]:
            #    continue
            current.append(nums[i])
            self.backtrack(nums, i+1, current, result)
            current.pop()


# 39. Combination Sum
class Solution_39(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []
        start = 0
        self.backtrack(candidates, start, current, result, target)
        return result
    
    def backtrack(self, nums, start, current, result, target):
        if sum(current) > target:
            return
        elif sum(current) == target:
            result.append(current[:])
        else:  
            for i in range(start, len(nums)):
                current.append(nums[i])
                self.backtrack(nums, i, current, result, target)
                current.pop()
        
        

# 40. Combination Sum II (can't reuse same element)
class Solution_40(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []
        start = 0
        candidates.sort()
        self.backtrack(candidates, start, current, result, target)
        return result
    
    def backtrack(self, nums, start, current, result, target):
        if sum(current) > target:
            return
        elif sum(current) == target: #and current not in result:
            result.append(current[:])
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                self.backtrack(nums, i+1, current, result, target)
                current.pop()


# 46. Permutations
class Solution_49(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        self.backtrack(nums, current, result)
        return result
    
    def backtrack(self, nums, current, result):
        if len(current) == len(nums):
            result.append(current[:])
        else:
            for n in nums:
                if n not in current: # element already exists, skip
                    current.append(n)
                    self.backtrack(nums, current, result)
                    current.pop()


# 47. Permutations II (contains duplicates)
import collections
class Solution_47(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current = []
        count = collections.Counter(nums)  # use count to show quota
        self.backtrack(nums, current, result, count)
        return result
    
    def backtrack(self, nums, current, result, count):
        if len(current) == len(nums):
            result.append(current[:])
        else:
            for n in count:
                if count[n] > 0:
                    current.append(n)
                    count[n] -= 1
                    self.backtrack(nums, current, result, count)
                    current.pop()
                    count[n] += 1


# * 131. Palindrome Partitioning
class Solution_131(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        current = []
        start = 0
        self.backtrack(s, start, current, result)
        return result
    
    def backtrack(self, s, start, current, result):
        if start == len(s):
            result.append(current[:])
        else:
            for i in range(start, len(s)):
                partion = s[start:i+1]
                if partion == partion[::-1]:
                    current.append(s[start:i+1])
                    self.backtrack(s, i+1, current, result)
                    current.pop()


# 83. Remove Duplicates from Sorted List
class Solution_83(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head


# 994. Rotting Oranges
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count_one = 0
        queue = collections.deque()
        minute = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count_one += 1
                elif grid[i][j] == 2:
                    queue.appendleft((i, j))
    
        while queue and count_one:
            for _ in range(len(queue)):
                i, j = queue.pop()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.appendleft((x, y))
                        count_one -= 1
            minute += 1

        return -1 if count_one else minute
                

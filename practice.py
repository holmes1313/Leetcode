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
class Solution(object):
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

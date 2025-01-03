"""
Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)"""
class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # with division operation
        total_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            result = []
            for num in nums:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            return result

        result = []
        for num in nums:
            result.append(total_product // num)
        return result

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_products = []
        right_products = []

        left_product = 1
        for num in nums:
            left_products.append(left_product)
            left_product *= num

        right_product = 1
        for num in nums[::-1]:
            right_products.append(right_product)
            right_product *= num

        n = len(nums)
        for i in range(n):
            left_products[i] *= right_products[n-i-1]
        return left_products


    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(1) extra space
        n = len(nums)
        ans = [1] * n

        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans

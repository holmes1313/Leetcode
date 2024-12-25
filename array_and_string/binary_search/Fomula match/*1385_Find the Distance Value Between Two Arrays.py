"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Constraints:
1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100
"""
class Solution(object):
    def findTheDistanceValue1(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        flag = 0 
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = 1
                    break
            if not flag:
                count += 1
            else:
                flag = 0
        return count

    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        def findDistance(arr2, f, to):
            p1 = 0
            p2 = len(arr2) - 1
            while p1 <= p2:
                mid = (p1 + p2) // 2
                if f <= arr2[mid] <= to:
                    return True
                elif arr2[mid] < f:
                    p1 = mid + 1
                elif arr2[mid] > to:
                    p2 = mid - 1

            return False

        arr2.sort()
        count = 0
        for num1 in arr1:
            if not findDistance(arr2, num1-d, num1+d):
                count += 1
        
        return count

        
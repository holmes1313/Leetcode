# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:41:47 2019

@author: z.chen7
"""

# 973. K Closest Points to Origin
"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  
The answer is guaranteed to be unique (except for the order that it is in.)


Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # sorted function
        #points_sorted = sorted(points, key=lambda p: (p[0])**2 + (p[1])**2)
        #return points_sorted[:K]
        
        # merge sort
        # self.sortPoints(points)
        
        # quick sort
        points = self.quickSortPoints(points)
        return points[:K]
        
        
    def mergeSortPoints(self, points):
        if len(points) > 1:
            mid = len(points) // 2
            left = points[:mid]
            right = points[mid:]
            
            self.sortPoints(left)
            self.sortPoints(right)
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if self.calculateDistance(left[i]) < self.calculateDistance(right[j]):
                    points[k] = left[i]
                    i += 1
                else:
                    points[k] = right[j]
                    j += 1
                k += 1
                
            while i < len(left):
                points[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                points[k] = right[j]
                j += 1
                k += 1
    
    def quickSortPoints(self, points):
        less = []
        equal = []
        greater = []
        
        if len(points) <= 1:
            return points
        
        pivot = points[0]
        pivot_distance = self.calculateDistance(pivot)
        
        for p in points:
            p_distance = self.calculateDistance(p)
            if p_distance < pivot_distance:
                less.append(p)
            elif p_distance > pivot_distance:
                greater.append(p)
            else:
                equal.append(p)
        return self.quickSortPoints(less) + equal + self.quickSortPoints(greater)
    
    def calculateDistance(self, point):
        return point[0] ** 2 + point[1] ** 2
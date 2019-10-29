"""
You are given an array of integers arr, representing a sequence of numerical tiles 
that you can stand on. Initially, you're standing on the first tile (arr[0]), 
and you can step forward by at most k tiles at a time. 
Your mission is to reach the final tile (arr[arr.length - 1]), and the value of 
each tile you stand on is added to your total score (including the first and last tile).

Your task is to find the maximal possible score you can achieve after reaching the end.

Example 1
For arr = [3, 4, -2, 1, 2] and k = 2, the output should be arrayTrip(arr, k) = 10.
Since k = 2, it's possible to skip over one tile by taking a step of size 2. 
We can get the best score by skipping over the negative tile (arr[2] = -2),
and visiting all the positive tiles. This gives a total of 3 + 4 + 1 + 2 = 10.

Example 2
For arr = [0, -3, -2, -5, -7, 1] and k = 3, the output should be arrayTrip(arr, k) = -1.
With k = 3, we could skip over a maximum of two tiles at a time, so we won't be 
able to avoid all the negative tiles. The best option is to visit the least 
negative value arr[2] = -2 and avoid the others. This gives a total of 0 + (-2) + 1 = -1.


From Obed:
It sounds like a sliding window problem
As you walk through each item, move one more step (less than k steps) and do your checks
For example 1 When you’re on item 4, you’ll first step one time to find -2. 
Now you step one more time (k = 2) and find 1. As you’re stepping through, you can compare and say (4 + -2) is less than (4 + 1)
3 questions total?"""


def arrayTrip(arr, k):
    if not arr:
        return None
    
    if len(arr) <= 2: 
        result = sum(arr)
    
    else:
        result = arr[0] + arr[-1]
        sub_arr = arr[1:-1]
        
        helper(sub_arr, k)
    
    
    arr = arr + [0] * k
    index = 1    
    
    while index < len(arr) - k:
        choice = {}
        for j in range(index+1, index+k+1):
            choice[arr[j]] = j
        m = max(choice.keys())
        result += m
        index = choice[m] 
        
    return result



def test():
    output = arrayTrip([3, 4, -2,1, 2], 2)
    




[2, 1].sort()

max(a.keys())
a = {'a': 1, 'b': 2, 'c': 1}
max(a, key=a.get)

import collections

def zombieClusters(zombies):
    
    if not zombies:
        return 0
    
    count = 0
    rn = len(zombies)
    cn = len(zombies[0])
    
    for i in range(rn):
        for j in range(cn):
            if zombies[i][j] == 1:
                count += 1
                findzombiecluster(zombies, i, j, rn, cn)
    return count
                

def findzombiecluster(zombies, i, j, rn, cn):
    queue = collections.deque()
    queue.appendleft((i, j))
    
    while queue:
        x, y = queue.pop()
        if zombies[x][y] == 1:
            zombies[x][y] = 2
            appendToQueue(queue, x-1, y, rn, cn)
            appendToQueue(queue, x+1, y, rn, cn)
            appendToQueue(queue, x, y-1, rn, cn)
            appendToQueue(queue, x, y+1, rn, cn)
            
            
def appendToQueue(queue, x, y, rn, cn):
    if (0 <= x < rn) and (0 <= y < cn):
        queue.appendleft((x, y))
            
    

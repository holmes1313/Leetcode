# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:16:03 2019

@author: z.chen7
"""
"""
There are n zombies in Seattle, and Liv and Ravi are trying to track them down 
to find out who is creating new zombies — thus preventing an apocalypse. 
Other than the patient-zero zombies (who became so by mixing MaxRager and tainted 
Utopium), new people only become zombies after being scratched by an existing zombie; 
for this reason, zombiism is transitive. This means that if zombie 0 knows zombie 1 
and zombie 1 knows zombie 2, then zombie 0 is connected to zombie 2. 
A zombie cluster is a group of zombies who are directly or indirectly linked 
through the other zombies they know (such as the one who scratched them or 
supplies them with brains).

Given an array of arrays of integers zombies that describes an n × n square 
matrix of known connected zombies; if zombies[i][j] = 0, then the i and j zombies 
do not know one another (otherwise, the cell contains a 1 and they do know one another). 
Your task is to return an integer denoting the number of zombie clusters Liv and Ravi have identified in Seattle.

Example 1
For
zombies = [[1, 1, 0, 0],
           [1, 1, 1, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]
the output  should be zombieClusters(zombies) = 2.
In this example, we're considering 4 zombies, which can be labelled Z_0 through Z_3. 
There are 2 pairs of zombies who directly know each another: (Z_0, Z_1) and (Z_1, Z_2). 
Because of zombiism's transitive property, the set of zombies {Z_0, Z_1, Z_2} is considered 
to be a single zombie cluster. The remaining zombie, Z_3, doesn't know any other zombies 
and is considered to be their own, separate zombie cluster ({Z_3}). 
This gives us a total of 2 zombie clusters, so the answer is 2.

Example 2
For
zombies = [[1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]
the output should be
zombieClusters(zombies) = 5.
No zombie knows any of the other zombies, so they each form their own zombie 
clusters: {Z_0}, {Z_1}, {Z_2}, {Z_3}, and {Z_4}. This means we have 5 zombie clusters, so the answer is 5.

Input/Output
[execution time limit] 4 seconds (py)
[input] array.array.integer zombies
A square matrix of known connected zombies; if zombies[i][j] = 0, 
then zombies i and j do not know one another (otherwise, the cell contains a 1 and they do know one another).

Guaranteed constraints:
1 ≤ zombies.length = zombies[i].length ≤ 300,
zombies[i][i] = 1,
zombies[i][j] = zombies[j][i]
"""


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



input = [[1,0,0,0,0,0,1,0,0,0], 
         [0,1,0,0,0,1,0,0,0,1], 
         [0,0,1,0,1,0,0,0,0,0], 
         [0,0,0,1,0,0,0,0,0,0], 
         [0,0,1,0,1,0,0,0,0,0], 
         [0,1,0,0,0,1,0,0,0,0], 
         [1,0,0,0,0,0,1,0,0,0], 
         [0,0,0,0,0,0,0,1,0,0], 
         [0,0,0,0,0,0,0,0,1,0], 
         [0,1,0,0,0,0,0,0,0,1]]
"""
Output:
18
Expected Output:
6
"""


Solution().numIslands(input)
zombieClusters(input)

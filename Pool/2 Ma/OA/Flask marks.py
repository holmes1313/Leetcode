"""
A robotic chemical delivery system for a college chemistry laboratory has been configured to work using only one type of glass flask per day. For each chemical ordered, it will be filled to a mark that is at least equal to the volume ordered. There are multiple flasks available, each with markings at various levels. Given a list of order requirements and a list of flasks with their measurements, determine the single type of flask that will result in minimal waste. Waste is the sum of marking - requirement for each order. Return the zero-based index of the flask type chosen. If there are multiple answers, return the minimum index. If no flask will satisfy the constraints, return -1.
Example
n = 4 (number of orders)
requirements = [4, 6, 6, 7]
flaskTypes = 3
markings = [[0, 31, [0, 51, [0, 7],
[1, 6], [1, 8], [1, 9],
[2, 3], [2, 5], [2, 6]]
The markings array is a 2D array where the first element is the flask number and the second an available marking. In this case, the first type has markings at 3, 5 and 7. The second type has them at 6, 8 and 9, and the third type has markings at 3, 5 and 6.
Using the first flask type, the losses are: 5 - 4 = 1, 7 - 6 = 1, 7 - 6 = 1, 7 - 7 = 0. 1 + 1 + 1 + 0 = 3 units
wasted.
Using the second flask type, losses are: 6 - 4 = 2, 6 - 6 = 0, 6 - 6 = 0, 8 - 7 = 1. 2 + 0 + 0 + 1 = 3 units
wasted.
The third flask type cannot be used because its maximum capacity is 6 and there is an order for 7.
Two types of flasks can be used and 3 units will be lost. The lower index flask is at index 0.
NOTE: The markings 2D array will be given in order of the flasks, i.e., the markings for the 0-index flask will be followed by markings of 1-index flask and so on. For each flask, the given markings will also be sorted in ascending order.
Function Description
Complete the function chooseFlask in the editor below.
chooseFlask has the following parameter(s):
int requirements[n]: the requirements for the orders int flasklypes: the number of flask types
int markings[totalMarks][2]: the first column signifies the index of the flask and second signifies one mark
Returns:
int: the index of the flask to choose or -1 if none will work
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chooseFlask' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER flaskTypes
#  3. 2D_INTEGER_ARRAY markings
#
import bisect
import collections


def chooseFlask(requirements, flaskTypes, markings):
    flask_markings = collections.defaultdict(list)
    
    for marking in markings:
        flask_markings[marking[0]].append(marking[1])
    
    max_req = max(requirements)
    min_wast = float('inf')
    best_flask_idx = -1
    memo = {}
    requirements.sort()
    for i in range(flaskTypes):
        markings = flask_markings[i]     
        if not markings or markings[-1] < max_req:
            # flask i can't be used
            continue

        curr_waste = 0        
        for j in range(len(markings)):
            mark = markings[j]
            # if markings[i] in memo:
            #     curr_waste += memo[markings[i]]
            if mark not in memo:
                memo[mark] = bisect.bisect_right(requirements, mark) 
            idx = memo[mark]
            if j == 0:
                last_idx = 0
            else:
                last_idx = memo[markings[j-1]]
            for diff in range(last_idx, idx):
                curr_waste += (mark - requirements[diff])
                
        if curr_waste < min_wast:
            min_wast = curr_waste
            best_flask_idx = i
            
    return best_flask_idx
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requirements_count = int(input().strip())

    requirements = []

    for _ in range(requirements_count):
        requirements_item = int(input().strip())
        requirements.append(requirements_item)

    flaskTypes = int(input().strip())

    markings_rows = int(input().strip())
    markings_columns = int(input().strip())

    markings = []

    for _ in range(markings_rows):
        markings.append(list(map(int, input().rstrip().split())))

    result = chooseFlask(requirements, flaskTypes, markings)

    fptr.write(str(result) + '\n')

    fptr.close()

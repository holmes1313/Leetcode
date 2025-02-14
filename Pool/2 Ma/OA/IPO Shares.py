"""
An initial public offering (IPO) refers to the process of offering shares of a private corporation to the public in a new stock issuance. Public share issuance allows a company to raise capital from public investors. IPO process can go through a typical auction, and an IPO price is not set before the auction. Potential buyers are able to bid for the shares they want and the price they are willing to pay. The bidders who were willing to pay the highest price are then allocated the shares available.
Before the auction ends, potential buyers can submit bids containing: user Id, number of shares, bidding price, timestamp.
Once all the bids are submitted, the allotted placement is assigned to the bidders from the highest bids down, until all of the allotted shares are assigned. The auction assigns shares in multiple rounds until all shares are allocated or no more bids. In each round, it finds the bids with highest prices, assigns the shares, and removes the assigned bids:
1. If the bid (with the highest price) has only 1 bidders, the bidder gets shares he/she bids for (or get whatever left if the unallocated shares are less than the bid shares);
2. If the bids (with the highest price) have multiple bidders, the bidders are assigned shares as follows:
Shares are distributed round robin style (i.e. one share per bidder in sequence until shares are all allocated) to bidders in the same price group, with the bidders sorted by timestamp. Once a bidder gets the number of shares they bid for, they will be removed from the above iterative process and the process which then continues until all bidders are removed or the shares get exhausted, whichever comes first.
Find out all bidders (user IDs) with no share allocation.
Function Description
Complete the function getResults in the editor below. The function must return a list of integers, each an Id for those bidders who receive no shares, sorted ascending.
getResults has the following parameter(s):
bids[bids[0],_bids[n-1]J: a 2D array of arrays of integers, Id, shares, price, timestamp named u, sc, bp, ts going forward
totalShares: an integer, the total shares to allocate
Constraints
•
・15nx104
• 1 5 u, sc, bp, ts, totalShares < 10°
"""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getResults' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY bids
#  2. INTEGER totalShares
#
import collections


def getResults(bids, totalShares):
    bid_rounds = collections.defaultdict(list)
    no_share_bidders = set()
    have_share_bidders = set()
    for bid in bids:
        user_id, requested_shares, price, ts = bid
        bid_rounds[price].append([user_id, requested_shares, ts])
        
    for price in sorted(bid_rounds.keys(), reverse=True):
        bid_list = bid_rounds[price]
        total_requested_shares = 0
        for bid1 in bid_list:
            total_requested_shares += bid1[1]
            
        if total_requested_shares <= totalShares:
            totalShares -= total_requested_shares
            for bid1 in bid_list:
                have_share_bidders.add(bid1[0])
            
        else:                        
            bid_list.sort(key=lambda x: x[2])
            while totalShares > 0:
                for bid2 in bid_list:
                    if bid2[1] > 0:
                        bid2[1] -= 1
                        totalShares -= 1
                        have_share_bidders.add(bid2[0])
                        if totalShares == 0:
                            break
                    else:
                        continue
                        
                        
            
    for bid in bids:
        user_id, requested_shares, price, ts = bid
        if user_id not in have_share_bidders:
            #if allocated_shares[user_id] == 0:
            no_share_bidders.add(user_id)
            
    return sorted(no_share_bidders)
         
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bids_rows = int(input().strip())
    bids_columns = int(input().strip())

    bids = []

    for _ in range(bids_rows):
        bids.append(list(map(int, input().rstrip().split())))

    totalShares = int(input().strip())

    result = getResults(bids, totalShares)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

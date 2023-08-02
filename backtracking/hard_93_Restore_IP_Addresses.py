"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtracking(curr, start, dots):
            if start == len(s) and dots == 4:
                result.append(".".join(curr))
                return

            if dots >= 4 or start > len(s):
                return

            for i in range(start, min(start+3, len(s))):
                digits = s[start: i+1]
                if 0<= int(digits)<=255 and str(int(digits)) == digits:
                    curr.append(digits)
                    backtracking(curr, i+1, dots+1)
                    curr.pop()

        result = []
        backtracking([], 0, 0)

        return result

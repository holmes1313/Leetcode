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
        if len(s) > 12:
            return []

        def backtracking(curr, start, section_count):
            if start == len(s) and section_count == 4:
                result.append(".".join(curr))
                return

            if start >= len(s) or section_count >= 4:
                return

            for i in range(start, min(start + 3, len(s))):
                section = s[start:i + 1]
                integer = int(section)
                if integer <= 255 and str(integer) == section:
                    # curr.append(section)
                    backtracking(curr + [section], i + 1, section_count + 1)
                    # curr.pop()

        result = []
        backtracking([], 0, 0)
        return result

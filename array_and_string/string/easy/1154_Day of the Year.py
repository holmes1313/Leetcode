"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41

"""
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        from datetime import datetime
        YYYY, MM, DD = map(int, date.split("-"))
        start = datetime(YYYY, 1, 1)
        end = datetime(YYYY, MM, DD)
        return (end - start).days + 1

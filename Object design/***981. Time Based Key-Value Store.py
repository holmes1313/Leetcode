"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""

class TimeMap(object):

    def __init__(self):
        self.key_time_map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.key_time_map:
            self.key_time_map[key] = []

        self.key_time_map[key].append((timestamp, value)) 
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.key_time_map:
            return ""
        # use binary search to find first ts that > given timestamp
        pairs = self.key_time_map[key]

        if timestamp < pairs[0][0]:
            return ""

        left = 0
        right = len(pairs) - 1
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return pairs[left-1][1]

        
from sortedcontainers import SortedDict
import bisect


class TimeMap(object):

    def __init__(self):
        self.key_to_timed_values = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.key_to_timed_values:
            self.key_to_timed_values[key] = SortedDict()

        self.key_to_timed_values[key][timestamp] = value
        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.key_to_timed_values:
            return ""

        ts_to_values = self.key_to_timed_values[key]
        ts_list = ts_to_values.keys()
        idx = bisect.bisect_right(ts_list, timestamp)
        if idx == 0:
            return ""
        return ts_to_values[ts_list[idx-1]]
        # left = 0
        # right = len(ts_list) - 1
        # while left <= right:
        #     mid = (left+right) // 2
        #     if ts_list[mid] <= timestamp:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # if left == 0:
        #     return ""
        # return ts_to_values[ts_list[left-1]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

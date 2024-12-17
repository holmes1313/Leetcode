"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence: ... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]

Output: [["a"]]
"""
import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # Get the normalized key for the string
        def generate_key(s):
            pattern = []
            for i in range(1, len(s)):
                # Calculate the difference between consecutive letters and normalize it
                diff = (ord(s[i]) - ord(s[i-1]) + 26) % 26
                pattern.append(diff)
            # Use a tuple because it is hashable and can be a dictionary key
            return tuple(pattern)

        groups = collections.defaultdict(list)
        for s in strings:
            key = generate_key(s)
            groups[key].append(s)

        return list(groups.values())

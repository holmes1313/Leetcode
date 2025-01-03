"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

 

Example 1:


Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
Example 2:


Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
Output: "the five boxing wizards jump quickly"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".
 

Constraints:

26 <= key.length <= 2000
key consists of lowercase English letters and ' '.
key contains every letter in the English alphabet ('a' to 'z') at least once.
1 <= message.length <= 2000
message consists of lowercase English letters and ' '.

"""
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        decode = {}
        key = key.replace(" ", "").lower()
        a_code = ord("a")
        keys = set()
        i = 0
        for cha in key:
            if cha not in keys:
                decode[cha] = chr(i + a_code)
                keys.add(cha)
                i += 1
            if i == 26:
                break


        ans = ""
        for cha in message:
            if cha.isalpha():
                ans += decode[cha]
            else:
                ans += cha

        return ans

    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        decode_map = {}
        a_code = ord("a")
        keys = set()
        i = 0
        for cha in key:
            if not cha.isalpha():
                continue

            if cha not in decode_map:
                decode_map[cha] = chr(i + a_code)
                i += 1

            if i == 26:
                break

        ans = ""
        for cha in message:
            if cha.isalpha():
                ans += decode_map[cha]
            else:
                ans += cha

        return ans

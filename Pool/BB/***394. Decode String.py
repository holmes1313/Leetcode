"""
https://www.1point3acres.com/bbs/thread-1034146-1-1.html
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the current number (may be more than one digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and the current number to the stack
                stack.append((current_string, current_num))
                current_string = ""  # Reset current string for the new substring inside brackets
                current_num = 0  # Reset the number as we'll accumulate it again for the new substring
            elif char == ']':
                # Pop the previous string and the repeat count from the stack
                prev_string, repeat_count = stack.pop()
                # Repeat the current string the number of times specified and append it to the previous string
                current_string = prev_string + current_string * repeat_count
            else:
                # Add the current character to the current string being built
                current_string += char
        
        return current_string

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for cha in s:
            if cha == "]":
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                stack.append(curr_str * int(curr_num))
            else:
                stack.append(cha)

        return "".join(stack)







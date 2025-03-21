# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop() # remove the [
                
                x = ''
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x
                
                stack.append(curr * int(x))

        return ''.join(stack)
        
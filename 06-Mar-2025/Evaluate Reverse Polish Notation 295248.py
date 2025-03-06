# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for op in tokens:
            if op in ops:
                op1 = stack.pop()
                op2 = stack.pop()
                if op == '+':
                    res = op2 + op1
                elif op == '-':
                    res = op2 - op1
                elif op == '*':
                    res = op2 * op1
                elif op == '/':
                    res = int(op2 / op1)
                stack.append(int(res))
            else:
                stack.append(int(op))  
                
        return stack.pop()

# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        res = self.myPow(x, abs(n)//2)
        res = res * res 

        if n % 2 != 0:
            res = res * x
            
        return res if n > 0 else 1/ res
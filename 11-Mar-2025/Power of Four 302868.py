# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

"""class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True

        if n % 4 != 0:
            return False
        

        return self.isPowerOfFour(n // 4)
"""
# iterative way
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        
        while n % 4 == 0:
            n //= 4
            
        return n == 1

# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def countGood(power: int, x: int) -> int:
            if power == 0:
                return 1
            elif power % 2 == 0:
                return countGood(power // 2, x * x % MOD)
            return x * countGood(power - 1, x) % MOD

        MOD = 10 ** 9 + 7
        
        return 5 ** (n % 2) * countGood(n // 2, 4 * 5) % MOD #
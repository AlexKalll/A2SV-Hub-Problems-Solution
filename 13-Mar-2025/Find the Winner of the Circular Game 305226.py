# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player = [a for a in range(1, n+1)]
        cur = 0
        while len(player) > 1:
            cur = (cur + k -1) % len(player)
            player.pop(cur)
        return player[0]

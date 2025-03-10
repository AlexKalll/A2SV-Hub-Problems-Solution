# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0
        i = 0

        for i in range(k):
            ans += (happiness[i] - i if happiness[i]-i > 0 else 0)
            i += 1
        
        return ans
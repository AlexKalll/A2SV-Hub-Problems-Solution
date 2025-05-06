# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        deltas = SortedList()
        pairs = 0
        for num1, num2 in zip(nums1, nums2):
            delta = num1 - num2
            pairs += deltas.bisect_right(delta + diff)
            deltas.add(delta)
            
        return pairs
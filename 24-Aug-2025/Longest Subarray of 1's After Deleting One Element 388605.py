# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        zero_cnt = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            while zero_cnt == 2:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            ans = max(ans, right - left)
            
        return ans
# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def backtrack(self, ans: List[str], arr: List[str], currCombo: str, n: int):
        
        if len(currCombo) == n:
            ans.append(currCombo)
            return
        for num in arr:
            if not len(currCombo) == 0 and num == "0" and currCombo[-1] == "0":
                continue
            currCombo += num
            self.backtrack(ans, arr, currCombo, n)
            
            currCombo = currCombo[:len(currCombo) - 1:1]
    
    def findAllCombinations(self, n: int) -> List[str]:
        ans = []
        arr = ["0", "1"]
        currCombo = ""
        self.backtrack(ans, arr, currCombo, n)
        return ans
    
    def validStrings(self, n: int) -> List[str]:
        return self.findAllCombinations(n)
# Problem: Combinations - https://leetcode.com/problems/combinations/

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [num for num in range(1, n+1)]
        
        combs = combinations(arr, k)
        ans = []

        for comb in combs:
            ans.append(list(comb))
        
        return ans
    """
# for loop implemetation

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(first_num, path):
            if len(path) == k:
                ans.append(path[:])
                return 

            for num in range(first_num, n+1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
            
        ans = []

        backtrack(1, [])

        return ans
"""     
# dp approach
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []   
        path = []

        def backtrack(i):
            if len(path) == k:
                ans.append(path[:])
                return
            # since we aren't using the for loop, it will not handle this case. so this case is used as a base case 
            if i > n:
                return 
            # include i
            path.append(i)
            backtrack(i + 1)
            
            # not include i
            path.pop()

            backtrack(i + 1)
        
        backtrack(1)

        return ans
"""
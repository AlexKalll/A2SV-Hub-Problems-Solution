# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "O":
                return
            
            grid[i][j] = "#"  # Mark as visited
            
            # Explore all four directions
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        # Step 1: Capture all 'O's on the border and mark them
        for i in range(rows):
            for j in range(cols):
                # Check the first and last row
                if (i == 0 or i == rows - 1) and grid[i][j] == "O":
                    dfs(i, j)
                # Check the first and last column
                if (j == 0 or j == cols - 1) and grid[i][j] == "O":
                    dfs(i, j)

        # Step 2: Flip all remaining 'O's to 'X's and '#' back to 'O's
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O":
                    grid[i][j] = "X"  # Flip surrounded 'O's to 'X'
                elif grid[i][j] == "#":
                    grid[i][j] = "O"  # Restore the marked 'O's


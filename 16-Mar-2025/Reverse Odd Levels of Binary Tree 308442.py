# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # in recursive manner
        def helper(r1, r2, depth):
            if not r1:
                return 
            if depth %2 != 0:
                temp = r1.val
                r1.val = r2.val
                r2.val = temp
            helper(r1.left, r2.right, depth +1)
            helper(r1.right, r2.left, depth +1)
        
        helper(root.left, root.right, 1)
        return root
"""
# in iterative manner as follows 
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            current_level_nodes = []
            
            for _ in range(size):
                node = queue.popleft()
                current_level_nodes.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 != 0:  # Check if the level is odd
                left, right = 0, size - 1
                while left < right:
                    # Swap values of nodes at odd levels
                    current_level_nodes[left].val, current_level_nodes[right].val = current_level_nodes[right].val, current_level_nodes[left].val
                    left += 1
                    right -= 1
            
            level += 1
        
        return root
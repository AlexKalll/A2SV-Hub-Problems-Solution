# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        merged_root = TreeNode(root1.val + root2.val)
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)

        return merged_root
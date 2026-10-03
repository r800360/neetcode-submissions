# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return - 1
        
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        self.diameter = max(self.diameter, left + right + 2)
        return 1 + max(left, right)
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.getHeight(root)
        return self.diameter
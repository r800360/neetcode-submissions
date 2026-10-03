# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, node: Optional[TreeNode]):
        if not node:
            return -1
        
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        if abs(left - right) > 1:
            self.isBalanced = False

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        self.getHeight(root)
        return self.isBalanced
        # if not root:
        #     return True
        # res1 = self.helper(root.left)
        # res2 = self.helper(root.right)
        # if res1 == False or res2 == False:
        #     return False
        
        # return abs(root.left.height - root.right.height) <= 1
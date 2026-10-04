# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversalHelper(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if not root:
            return
        result.append(root.val)
        self.preorderTraversalHelper(root.left, result)
        self.preorderTraversalHelper(root.right, result)
        return result
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = self.preorderTraversalHelper(root, [])
        return preorder if preorder else []
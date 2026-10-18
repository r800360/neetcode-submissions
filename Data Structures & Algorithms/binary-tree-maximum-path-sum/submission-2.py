# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1001

        # maximum path sum starting at this node and extending downward in at most one direction
        def dfs(node):
            nonlocal result
            
            if not node:
                return 0

            # Ignore negative contributions from either subtree
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best path whose highest point is this node
            result = max(result, node.val + left + right)

            # Return a path that can extend to the parent
            return node.val + max(left, right)

        dfs(root)
        return result
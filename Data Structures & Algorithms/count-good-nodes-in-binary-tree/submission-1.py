# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good_nodes = 1

        while stack:
            node, value = stack.pop()

            if node.right:
                stack.append((node.right, max(node.right.val, value)))
                if node.right.val >= value:
                    good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.left.val, value)))
                if node.left.val >= value:
                    good_nodes += 1
        
        return good_nodes
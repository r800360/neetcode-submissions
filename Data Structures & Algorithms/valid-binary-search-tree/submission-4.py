# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        len_result = 0
        stack = []
        current = root

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Reached leftmost node
            current = stack.pop()
            result.append(current.val)
            if len(result) > 1 and result[-1] <= result[-2]:
                return False

            # Explore right subtree
            current = current.right
        
        # for i in range(len(result)-1):
        #     if result[i+1] <= result[i]:
        #         return False

        return True
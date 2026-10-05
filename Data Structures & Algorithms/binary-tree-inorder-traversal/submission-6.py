# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right 

            else:
                # Find the rightmost node in the left subtree
                pred = current.left

                while pred.right and pred.right != current:
                    pred = pred.right

                if not pred.right:
                    # Temporary link back to current
                    pred.right = current
                    current = current.left

                else:
                    # Returned from left subtree
                    pred.right = None
                    result.append(current.val)
                    current = current.right

        return result
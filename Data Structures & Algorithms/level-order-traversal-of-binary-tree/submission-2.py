# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                element = queue.popleft()
                level.append(element.val)
                if element.left:
                    queue.append(element.left)

                if element.right:
                    queue.append(element.right)
            
            result.append(level)

        return result
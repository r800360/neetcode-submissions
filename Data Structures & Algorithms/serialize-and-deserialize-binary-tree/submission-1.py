# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = [root]
        result = []

        while queue:
            node = queue.pop(0)

            if not node:
                result.append(-1001)
            else:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        while result and result[-1] == -1001:
            result.pop()
        
        return ",".join(map(str, result))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        result = list(map(int, data.split(",")))
        print(result)
        root = TreeNode(result[0])
        queue = [root]
        i = 1

        while queue:
            node = queue.pop(0)

            if i < len(result):
                if result[i] != -1001:
                    node.left = TreeNode(result[i])
                    queue.append(node.left)
                i += 1

            if i < len(result):
                if result[i] != -1001:
                    node.right = TreeNode(result[i])
                    queue.append(node.right)
                i += 1
        
        return root

        
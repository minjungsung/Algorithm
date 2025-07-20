# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(node, path):
            if not node: return []

            path += ('->' if path != '' else '')+ str(node.val)

            if node.left == node.right:
                return [path]
            else:
                return traverse(node.right, path) + traverse(node.left, path)
            
        return traverse(root, '')


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        def loop(root, res):
            print(root, res)
            if root:
                res.append(root.val)
            if root.left:
                loop(root.left, res)
            if root.right:
                loop(root.right, res)
        temp = loop(root, result)
        print(result)
        return result
        


        
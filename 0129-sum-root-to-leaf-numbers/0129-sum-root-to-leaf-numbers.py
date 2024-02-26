# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], string="") -> int:
        if root.left is None and root.right is None:
            string += str(root.val)
            return int(string)
        string += str(root.val)
        lp, rp = 0, 0
        if root.left:
            lp = self.sumNumbers(root.left, string)
        if root.right:
            rp = self.sumNumbers(root.right, string)
        return lp + rp
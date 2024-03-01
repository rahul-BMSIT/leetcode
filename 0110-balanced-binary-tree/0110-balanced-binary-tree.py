# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ischk = True
        def depth(node):
            if not node:
                return 0
            
            leftn = depth(node.left)
            rightn = depth(node.right)

            if leftn is None or rightn is None:  
                return None

            if leftn - rightn > 1 or leftn - rightn < -1:
                self.ischk = False
            else:
                return max(leftn, rightn) + 1

        depth(root)
        return self.ischk
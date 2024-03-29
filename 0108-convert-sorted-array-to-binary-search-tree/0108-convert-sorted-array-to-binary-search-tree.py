# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return
        ind=len(nums)//2           
        root=TreeNode(nums[ind])   
        root.left=self.sortedArrayToBST(nums[:ind])     
        root.right=self.sortedArrayToBST(nums[ind+1:])
        return root

        
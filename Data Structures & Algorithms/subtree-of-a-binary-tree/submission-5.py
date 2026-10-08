# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,sub):
            if not root and not sub:
                return True
            if root and sub and root.val==sub.val:
                return sameTree(root.left,sub.left) and sameTree(root.right,sub.right)
            return False
        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        

        
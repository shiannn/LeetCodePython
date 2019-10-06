# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visit = []
        self.inorderTraversalutil(root,visit)
        return visit
    def inorderTraversalutil(self,root,visit):
        if(root == None):
            return
        self.inorderTraversalutil(root.left,visit)
        visit.append(root.val)
        self.inorderTraversalutil(root.right,visit)
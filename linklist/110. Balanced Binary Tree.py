# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        DepthL = self.GetDepth(root.left)
        DepthR = self.GetDepth(root.right)
        if(abs(DepthL-DepthR)>1):
            return False
        flagL = self.isBalanced(root.left)
        if(flagL == False):
            return False
        flagR = self.isBalanced(root.right)
        if(flagR == False):
            return False
        return True
    
    def GetDepth(self,root):
        if(root == None):
            return 0
        DepthL = self.GetDepth(root.left)
        DepthR = self.GetDepth(root.right)

        return (1+max(DepthL,DepthR))

if __name__ == '__main__':
    sol = Solution()
    root3 = TreeNode(3)
    root9 = TreeNode(9)
    root20 = TreeNode(20)
    root15 = TreeNode(15)
    root7 = TreeNode(7)
    root3.left = root9
    root3.left = root20
    root20.left = root15
    root20.left = root7 
    depth = sol.GetDepth(root3)
    ans = sol.isBalanced(root3)
    print(ans)
        
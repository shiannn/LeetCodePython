import time

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        L = len(preorder)
        ret = self.buildTreeutil(preorder,0,L,inorder,0,L)
        return ret
    def buildTreeutil(self,preorder,PreLeft,PreRight,inorder,InLeft,InRight):
        #print(PreLeft,PreRight)
        #time.sleep(0.2)
        if(PreLeft>=PreRight):
            return None
        else:
            rootNode = TreeNode(preorder[PreLeft])
            for k in range(len(inorder)):
                if(preorder[PreLeft] == inorder[k]):
                    break
            rootNode.left = self.buildTreeutil(preorder,PreLeft+1,PreLeft+(k-InLeft+1),inorder,InLeft,k)
            rootNode.right = self.buildTreeutil(preorder,PreLeft+(k-InLeft+1),PreRight,inorder,k+1,InRight)
            return rootNode
    
    def printTree(self,root):
        if(root != None):
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

if(__name__ == '__main__'):
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    ans = sol.buildTree(preorder,inorder)
    sol.printTree(ans)
    
        
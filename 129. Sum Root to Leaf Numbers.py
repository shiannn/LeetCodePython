#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        global TotalSum
        TotalSum = 0
        self.dfs(root,0)
        return TotalSum

    def dfs(self,root,TempSum):
        Temp = root.val + TempSum*10 
        if(root.left == None and  root.right == None):
            global TotalSum
            TotalSum += Temp 
        else:
            if(root.left != None):
                self.dfs(root.left,Temp)
            if(root.right != None):
                self.dfs(root.right,Temp)
    def CreateTree(self,numList):
        NodeList = [TreeNode(x) if x!=None else None for x in numList]
        L = len(NodeList)
        for i in range(L):
            if(i*2+1<L and i*2+2<L and NodeList[i] != None):
                NodeList[i].left = NodeList[i*2+1]
                NodeList[i].right = NodeList[i*2+2]
        return NodeList[0]
    def printTree(self,root):
        if(root == None):
            return
        else:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

if __name__ == '__main__':
    sol = Solution()
    A = [1,2,3]
    B = [4,9,0,5,1]
    root = sol.CreateTree(B)
    sol.printTree(root)
    
    ans = sol.sumNumbers(root)
    print(ans)
        
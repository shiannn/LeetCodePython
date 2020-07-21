#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if(root == None):
            return []
        TempPath = []
        AllPath = []
        self.dfs(root,0,sum,TempPath,AllPath)
        return AllPath
    def dfs(self,root,TempSum,Target,TempPath,AllPath):
        TempSum+=root.val
        TempPath.append(root.val)
        if(root.left == None and root.right == None):
            if(TempSum == Target):
                toput = TempPath[:]
                AllPath.append(toput)  
        else:
            if(root.left != None):
                self.dfs(root.left,TempSum,Target,TempPath,AllPath)
            if(root.right != None):
                self.dfs(root.right,TempSum,Target,TempPath,AllPath)
        TempPath.pop()
        return

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
    A = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
    sol = Solution()
    Tree = sol.CreateTree(A)
    #print(Tree)
    #sol.printTree(Tree)
    ans = sol.pathSum(Tree,22)
    print(ans)
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root == None):
            return []
        currentQueue = [[root]]
        retQueue = [[root.val]]
        self.BFS(currentQueue,retQueue)
        return retQueue
    def BFS(self,currentQueue,retQueue):
        while(len(currentQueue)>0):
            layer = currentQueue.pop(0)
            temp = []
            for start in layer:
                if(start.left != None):
                    temp.append(start.left)
                if(start.right != None):
                    temp.append(start.right)
            if(temp != []):
                retQueue.append([x.val for x in temp])
                currentQueue.append(temp)
           
    
if(__name__ == "__main__"):
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
        
    sol = Solution()
    ans = sol.levelOrder(a)
    print(ans)
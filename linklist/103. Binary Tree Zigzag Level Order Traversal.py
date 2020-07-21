# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        toStart = [[root]]
        if(root == None):
            return []
        ret = [[root.val]]
        count = 1
        while(toStart != [[]]):
            stList = toStart.pop()
            LayerList = []
            for st in stList:
                if(st != None):
                    LayerList.append(st.left)
                    LayerList.append(st.right)
            toStart.append(LayerList)
            To_add = [x.val for x in LayerList if x != None]
            if(count % 2 == 1):
                To_add.reverse()
            if(To_add != []):
                ret.append(To_add)
            count += 1
        return ret
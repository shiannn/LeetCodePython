class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Utils:
    def createFromList(self, inputList):
        head, tail = None, None
        for l in inputList:
            tmp = ListNode(l)
            if(head == None):
                head, tail = tmp, tmp
            else:
                tail.next = tmp
                tail = tmp
        return head
    def printLinkList(self, head):
        ptr = head
        while(ptr):
            print(ptr.val)
            ptr = ptr.next

    def createTree(self, inputList):
        if len(inputList) == 0:
            return None
        TreeNodeList = [TreeNode(n) for n in inputList]
        for idx, tnode in enumerate(TreeNodeList):
            if idx*2 + 1 < len(TreeNodeList):
                tnode.left = TreeNodeList[idx*2+1]
            if idx*2 + 2 < len(TreeNodeList):
                tnode.right = TreeNodeList[idx*2+2]
        root = TreeNodeList[0]
        return root
    def printTree(self, root):
        if(not root):
            return
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([1,3,2,-3,-2,5,5,-5,1])
    t = util.createTree([1,3,2,-3,-2,5,5,-5,1])
    util.printTree(t)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if(not root):
            return False
        return(self.isPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right))

    def isPath(self, head, root) -> bool:
        if not head:
            return True
        if not root:
            return False
        ### root and head
        if root.val != head.val:
            return False
        else:
            return (self.isPath(head.next, root.left) or self.isPath(head.next, root.right))

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    head = util.createFromList([1,3,2])
    root = util.createTree([1,3,3,2,2,2,2,5,5])
    sol = Solution()
    ret = sol.isSubPath(head, root)
    print(ret)
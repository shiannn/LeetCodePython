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

    def findMidNode(self, head):
        slow, fast = head, head
        pre = slow
        while(fast.next and fast.next.next):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre != slow:
            pre.next = None
        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)

        mid = self.findMidNode(head)
        midNode = TreeNode(val=mid.val)
        if head != mid:
            midNode.left = self.sortedListToBST(head)
        midNode.right = self.sortedListToBST(mid.next)
        return midNode
    
    def printTree(self, head):
        if head == None:
            return
        print(head.val)
        self.printTree(head.left)
        self.printTree(head.right)

if __name__ == '__main__':
    sol = Solution()
    A = [1,1,0,4,2,2,3,5,6,7]
    head = sol.createFromList(A)
    root = sol.sortedListToBST(head)
    #print(root.val)
    sol.printTree(root)
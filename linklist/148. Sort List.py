# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            ### above 2 Nodes
            mid = self.getMid(head)
            left, right = head, mid.next
            mid.next = None
            sortedL = self.sortList(left)
            sortedR = self.sortList(right)
            merged = self.merge(sortedL, sortedR)
            return merged
    
    def merge(self, left, right):
        ### [10,30,50,70,90] [2,4,6,8]
        ptrL, ptrR = left, right
        dummyNode = ListNode(-1)
        tail = dummyNode
        while(ptrL and ptrR):
            if ptrL.val < ptrR.val:
                tail.next = ptrL
                ptrL = ptrL.next
            else:
                tail.next = ptrR
                ptrR = ptrR.next
            tail = tail.next
        if ptrL:
            tail.next = ptrL
        if ptrR:
            tail.next = ptrR
        return dummyNode.next

        
    def getMid(self, head):
        slow, fast = head, head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([4,19,14,5,-3,1,8,5,11,15])
    sol = Solution()
    ret = sol.sortList(l)
    util.printLinkList(ret)
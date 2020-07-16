# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

    def printList(self, head):
        ptr = head
        while(ptr!=None):
            print(ptr.val)
            ptr = ptr.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None):
            return None
        elif(head.next == None):
            return head
        ### head is not None and head.next is not None
        if(head.next.val != head.val):
            # head.next is also a start
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            # head.next is not a start, find the next start
            ptr = head.next
            while(ptr and ptr.val == head.val):
                ptr = ptr.next
            
            #head.next = self.deleteDuplicates(ptr)
            return self.deleteDuplicates(ptr)

sol = Solution()

A = [1,1,2,2,3]
B = [0]
ret = sol.createFromList(A)
ret_d = sol.deleteDuplicates(ret)
sol.printList(ret_d)
        
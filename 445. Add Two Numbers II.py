# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
                
        carry = 0
        to_next = None
        while stack1 and stack2:
            add = stack1.pop() + stack2.pop() + carry
            if add >= 10:
                add -= 10
                carry = 1
            else:
                carry = 0
            listNode = ListNode(val = add)
            listNode.next = to_next
            to_next = listNode
        stack = stack1 if stack1 else stack2
        while stack:
            add = stack.pop() + carry
            if add >= 10:
                add -= 10
                carry = 1
            else:
                carry = 0
            listNode = ListNode(val = add)
            listNode.next = to_next
            to_next = listNode
        
        if carry:
            listNode = ListNode(val = carry)
            listNode.next = to_next
            to_next = listNode

        return to_next

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    A = [5]
    B = [5]
    l1 = util.createFromList(A)
    l2 = util.createFromList(B)
    sol = Solution()
    root = sol.addTwoNumbers(l1, l2)
    while root:
        print(root.val)
        root = root.next
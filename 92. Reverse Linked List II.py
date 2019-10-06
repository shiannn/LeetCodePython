# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(0)
        preHead.next = head
        pre = preHead
        i = 0
        while(i != m-1):
            pre = pre.next
            i += 1
        #pre is in (m-1)
        cur = pre.next
        #cur is in (m)
        i = m+1
        while(i <= n):
            target = cur.next
            cur.next = target.next
            target.next = pre.next
            pre.next = target
            i += 1
        return preHead.next

Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(5)
sol = Solution()
ptr = Head
while(ptr != None):
    print(ptr.val)
    ptr = ptr.next
ans = sol.reverseBetween(Head,2,4)
ptr = Head
while(ptr != None):
    print(ptr.val)
    ptr = ptr.next



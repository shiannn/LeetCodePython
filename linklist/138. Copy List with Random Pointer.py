# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        old2new = {}
        headnew = Node(head.val)
        old2new[head] = headnew
        prev, ptr = headnew, head.next
        while(ptr):
            n = Node(ptr.val)
            old2new[ptr] = n
            prev.next = n
            prev, ptr = n, ptr.next
        ptr, ptrNew = head, headnew
        while(ptr):
            if ptr.random == None:
                ptrNew.random = None
            else:
                ptrNew.random = old2new[ptr.random]
            ptr, ptrNew = ptr.next, ptrNew.next
        return headnew
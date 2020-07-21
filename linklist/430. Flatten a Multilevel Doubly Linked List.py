# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        ptr = head
        while(ptr):
            if(ptr.child):
                flattened_child = self.flatten(ptr.child)
                if(ptr.next):
                    child_tail = self.getTail(flattened_child)
                    ptr.next.prev = child_tail
                    child_tail.next = ptr.next
                ptr.next = flattened_child
                flattened_child.prev = ptr
                ptr.child = None
            ptr = ptr.next

        return head
    
    def getTail(self, head):
        ptr = head
        while(ptr.next):
            ptr = ptr.next
        return ptr
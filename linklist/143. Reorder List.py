# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #util.printLinkList(head)
        idx, ptr = 0, head
        idx2Node = {}
        Node2idx = {}
        while(ptr):
            idx2Node[idx] = ptr
            Node2idx[ptr] = idx
            idx += 1
            ptr = ptr.next
        totalNum = idx - 1
        ptr, prev = head, None
        while(ptr):
            prev = ptr
            ptr = ptr.next
            ### deal with prev
            idx = Node2idx[prev]
            if idx > (totalNum / 2):
                N = totalNum + 1
            else:
                N = totalNum
            if N - idx == idx:
                prev.next = None
            else:
                prev.next = idx2Node[N - idx]
        return

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([])
    sol = Solution()
    sol.reorderList(l)
    util.printLinkList(l)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
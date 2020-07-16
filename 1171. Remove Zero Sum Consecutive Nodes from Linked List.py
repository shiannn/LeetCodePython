# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        seenNodeVal = {}
        curSum = 0
        dummyNode = ListNode(0)
        dummyNode.next = head
        ptr = dummyNode
        while(ptr != None):
            curSum += ptr.val
            #print('curSum', curSum)
            if(curSum in seenNodeVal):
                #seenNodeVal[curSum] = ptr
                # node already remove? 1 3 2
                tNode = seenNodeVal[curSum].next
                tsum = curSum + tNode.val
                while(tsum != curSum):
                    seenNodeVal.pop(tsum)
                    tNode = tNode.next
                    tsum += tNode.val
                seenNodeVal[curSum].next = ptr.next
                
            else:
                seenNodeVal[curSum] = ptr
            ptr = ptr.next

        return dummyNode.next

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([1,3,2,-3,-2,5,5,-5,1])
    sol = Solution()
    ret = sol.removeZeroSumSublists(l)
    while(ret != None):
        print(ret.val)
        ret = ret.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> list:
        l = self.getLength(root)
        eachPart = self.getEachPart(l, k)
        ans, head = [], root
        for numEach in eachPart:
            #print(numEach)
            ans.append(head)
            for n in range(numEach):
                prev = head
                head = head.next
                if n == numEach - 1:
                    prev.next = None
        return ans

    def getEachPart(self, l, k):
        eachPart = [l // k]*(k+1)
        for i in range(1,(l%k)+1):
            eachPart[i] += 1
        return eachPart[1:]

    def getLength(self, root):
        length, ptr = 0, root
        while(ptr):
            length += 1
            ptr = ptr.next
        return length

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([1,3,2,-3,-2,5,5,-5,1])
    sol = Solution()
    ret = sol.splitListToParts(l, 9)
    """
    while(ret != None):
        print(ret.val)
        ret = ret.next
    """
    for r in ret:
        ptr = r
        while(ptr != None):
            print(ptr.val)
            ptr = ptr.next
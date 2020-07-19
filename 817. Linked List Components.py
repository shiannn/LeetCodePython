# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: list) -> int:
        isIn = {}
        #isIn = [0] * 10010
        for g in G:
            isIn[g] = True
        ptr, ans, isStart = head, 1, True
        while(ptr):
            if not isIn.get(ptr.val):
                if(not isStart):
                    if(ptr.next):
                        ans += 1
                        isStart = True
                else:
                    if(not ptr.next):
                        ans -= 1
            else:
                isStart = False
            ptr = ptr.next
        return ans

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([0,1,2])
    G = [0,1]
    sol = Solution()
    ret = sol.numComponents(l, G)
    print(ret)
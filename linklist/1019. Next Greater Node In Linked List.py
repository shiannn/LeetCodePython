# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> list:
        stack, ptr = [], head
        tmp, idx = [], 0
        while(ptr):
            tmp.append((ptr.val, idx))
            ptr = ptr.next
            idx += 1
        ans = [0]* idx
        for num, idx in tmp:
            while(stack and num > stack[-1][0]):
                toNum, toIdx = stack.pop()
                ans[toIdx] = num
            stack.append((num, idx))
        return ans
    
    def getLength(self, head):
        ptr, length = head, 0
        while(ptr):
            length += 1
            ptr = ptr.next
        return length

if __name__ == '__main__':
    from utils import Utils
    util = Utils()
    l = util.createFromList([4,19,14,5,-3,1,8,5,11,15])
    #l = util.createFromList([])
    sol = Solution()
    ret = sol.nextLargerNodes(l)
    print(ret)
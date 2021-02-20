import collections

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        ret = []
        tail = -1
        N = len(num)
        already_remove = 0
        for i in range(N):
            #while(tail != -1 and tail+1+(N-i)>k and num[i] < ret[tail]):
            while(tail != -1 and already_remove<k and num[i] < ret[tail]):
                ret.pop()
                tail -= 1
                already_remove += 1
            ret.append(num[i])
            tail += 1
        ### get the N-k digits
        ret = ret[:N-k]
        ret = collections.deque(ret)
        ### remove leading zeros
        while(ret and ret[0] == '0'):
            ret.popleft()
        return ''.join(list(ret)) if ret else '0'

    def removeKdigits2(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        ret = []
        tail = -1
        N = len(num)
        already_remove = 0
        for i in range(N):
            #while(tail != -1 and tail+1+(N-i)>k and num[i] < ret[tail]):
            while(tail != -1 and already_remove<k and num[i] < ret[tail]):
                ret.pop()
                tail -= 1
                already_remove += 1
            ret.append(num[i])
            tail += 1
        ### get the N-k digits
        ret = ret[:N-k]
        ### remove leading zeros
        non_zero = 0
        for r in range(len(ret)):
            if ret[r] != '0':
                non_zero += 1
        if non_zero != 0:
            for r in range(len(ret)):
                if ret[r] != '0':
                    return ''.join(ret[r:])
        else:
            return '0'

if __name__ == '__main__':
    sol = Solution()
    num = "1432219"
    k = 3
    #num = "10200"
    #k = 1
    #num = "10"
    #k = 2
    #num = "1000"
    #k = 1
    num="112"
    k=1
    ret = sol.removeKdigits(num, k)
    print(ret)
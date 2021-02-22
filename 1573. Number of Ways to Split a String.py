class Solution:
    def numWays(self, s: str) -> int:
        numOnes = 0
        for ss in s:
            if ss == '1':
                numOnes += 1
        if numOnes % 3 != 0:
            return 0
        elif numOnes == 0:
            ret = ((len(s)-1)* (len(s)-2) // 2)% (1e9+7)
            return  int(ret)
        else:
            cur_numOnes = 0
            l, r = 0, 0
            for ss in s:
                if ss == '1':
                    cur_numOnes += 1
                if cur_numOnes == numOnes // 3:
                    l += 1
                elif cur_numOnes == 2* numOnes // 3:
                    r += 1
            #print(l, r)
            return int(l* r % (1e9+7))

    def numWays2(self, s: str) -> int:
        numOnes = 0
        for ss in s:
            if ss == '1':
                numOnes += 1
        if numOnes % 3 != 0:
            return 0
        elif numOnes == 0:
            ### C^(len(s) - 1)_2
            a1 = int((len(s)-1)% (1e9+7))
            a2 = int((len(s)-2)% (1e9+7))
            ret = int((a1* a2 // 2)% (1e9+7))
            return  ret
        else:
            ptr1 = numOnes // 3
            ptr2 = numOnes // 3
            #print(ptr1, ptr2)
            cur = 0
            while(ptr1 > 0):
                if s[cur] == '1':
                    ptr1 -= 1
                cur += 1
            #print(cur)
            zero1 = 0
            while(s[cur] == '0'):
                #print(cur)
                zero1 += 1
                cur += 1
            #print(cur)
            while(ptr2 > 0):
                #print('ptr2', ptr2)
                if s[cur] == '1':
                    ptr2 -= 1
                cur += 1
            #print(cur)
            zero2 = 0
            while(s[cur] == '0'):
                #print(cur)
                zero2 += 1
                cur += 1
            #print(cur)
            #print(zero1, zero2)
            return int(((zero1+1)* (zero2+1)) % (1e9+7))
                

if __name__ == '__main__':
    sol = Solution()
    #s = "10101"
    s = "100100010100110"
    #s = "0000"
    ret = sol.numWays(s)
    print(ret)
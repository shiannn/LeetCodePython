class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        AA, BB, CC = [], [], []
        for idx, ss in enumerate(s):
            if ss == 'a':
                AA.append(idx)
            elif ss == 'b':
                BB.append(idx)
            elif ss == 'c':
                CC.append(idx)
        AA.append(-1)
        BB.append(-1)
        CC.append(-1)
        #print(AA, BB, CC)
        nextA, nextB, nextC = [], [], []
        ptra, ptrb, ptrc = 0, 0, 0
        for idx, ss in enumerate(s):
            nextA.append(AA[ptra])
            nextB.append(BB[ptrb])
            nextC.append(CC[ptrc])
            if ss == 'a':
                ptra += 1
            elif ss == 'b':
                ptrb += 1
            elif ss == 'c':
                ptrc += 1
        #print(nextA, nextB, nextC)
        ret = 0
        for idx in range(len(s)):
            if nextA[idx]==-1 or nextB[idx]==-1 or nextC[idx]==-1:
                break
            complete_pos = max(nextA[idx], nextB[idx], nextC[idx])
            #print(len(s) - complete_pos)
            ret += len(s) - complete_pos
        #print(ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #s = "abcabc"
    #s = "aaacb"
    s = "abc"
    ret = sol.numberOfSubstrings(s)
    print(ret)
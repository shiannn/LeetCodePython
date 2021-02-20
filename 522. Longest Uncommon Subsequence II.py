class Solution:
    def findLUSlength1(self, strs):
        A = {}
        for s in strs:
            if s not in A:
                A[s] = 1
            else:
                A[s] += 1
        #print(A)
        sorted_strs = sorted(strs, key=len, reverse=True)
        #print(sorted_strs)
        for s in sorted_strs:
            if A[s] > 1:
                pass
            else:
                return len(s)
        return -1
    def findLUSlength(self, strs):
        N = len(strs)
        maxi = -1
        for i in range(N):
            #print(strs[i])
            isSub = False
            for j in range(N):
                if i == j:
                    continue
                isSub = isSub or self.isSubsequence(strs[i], strs[j])
            if not isSub:
                maxi = max(maxi, len(strs[i]))
        return maxi
    
    def isSubsequence(self, small, big):
        M = len(small)
        N = len(big)
        n = 0
        m = 0
        while(n != N):
            if small[m] == big[n]:
                m += 1
                if m == M:
                    return True
            n += 1
        return False

if __name__ == '__main__':
    sol = Solution()
    strs = ["aba", "cdc", "eae"]
    #strs = ["abab", "cdc", "eae"]
    #strs = ["aba", "aba", "cdc", "cdc"]
    ret = sol.findLUSlength(strs)
    print(ret)
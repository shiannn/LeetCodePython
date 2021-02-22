class Solution:
    def subarraysDivByK(self, A, K) -> int:
        mod2num = {0:1}
        sum_ = 0
        ret = 0
        for a in A:
            #print(a, mod2num)
            sum_ += a
            mod = (sum_ % K)
            if mod in mod2num:
                ret += mod2num[mod]
            if mod not in mod2num:
                mod2num[mod] = 1
            else:
                mod2num[mod] += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    A = [4,5,0,-2,-3,1]
    K = 5
    ret = sol.subarraysDivByK(A, K)
    print(ret)
class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        min_len = min([len(s) for s in strs])
        ret = 0
        for i in range(min_len):
            prefix = strs[0][i]
            for s in strs[1:]:
                if s[i] != prefix:
                    return "" if ret == 0 else strs[0][:ret]
            ret += 1
        return "" if ret == 0 else strs[0][:ret]
        
if __name__ == '__main__':
    sol = Solution()
    strs = ["flower","flow","flight"]
    #strs = ["dog","racecar","car"]
    #strs = []
    ret = sol.longestCommonPrefix(strs)
    print(ret)
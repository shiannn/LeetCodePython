class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_s, max_l = "", -1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                #if len(s[i:j+1]) > 5:
                isnice = self.isNice(s[i:j+1])
                #print(s[i:j+1], isnice)
                if isnice and len(s[i:j+1]) > max_l:
                    max_s = s[i:j+1]
                    max_l = len(s[i:j+1])
        return max_s
                    

    def isNice(self, s) -> bool:
        S = set({})
        for ss in s:
            #print(ss, ord(ss))
            S.add(ss)
        for ss in s:
            if ord(ss) >= 97:
                if chr(ord(ss)-32) not in S:
                    return False
            else:
                if chr(ord(ss)+32) not in S:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    #s = "YazaAay"
    #s = "Bb"
    #s = "c"
    s = "dDzeE"
    ret = sol.longestNiceSubstring(s)
    print(ret)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==0):
            return 0
        elif(len(s)==1):
            return 0 if(s[0]=='0') else 1
        #len is at least 2
        dp = [0]*len(s)
        if(s[0]=='0'):
            return 0
        else:
            dp[0] = 1
            if(s[1]!='0'):
                dp[1] = dp[0]
            temp = 10*int(s[0])+int(s[1])
            if(s[0]!='0' and temp<=26 and temp>=1):
                dp[1] = dp[1]+1

        for i in range(2,len(s)):
            if(s[i]!='0'):
                dp[i] = dp[i-1]
            temp = 10*int(s[i-1])+int(s[i])
            if(s[i-1]!='0' and temp<=26 and temp>=1):
                dp[i] = dp[i] + dp[i-2]
        print(dp)
        return dp[len(s)-1]


if __name__=='__main__':
    sol = Solution()
    inpu = "101"
    ans = sol.numDecodings(inpu)
    print(ans)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i,-1,-1):
                #前i個字
                #print('i==',i,'j==',j)
                #print(dp[j],s[0:j],s[j:i],(s[j:i] in wordDict))
                if((dp[j]==True) and (s[j:i] in wordDict)):
                    dp[i] = True
                    continue
        #print(dp[len(s)])
        return dp[len(s)]

if __name__=='__main__':
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    ans = sol.wordBreak(s,wordDict)
    #print(ans)
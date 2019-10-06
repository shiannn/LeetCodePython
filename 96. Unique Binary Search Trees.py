class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(0,i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

if(__name__ == '__main__'):
    sol = Solution()
    ans = sol.numTrees(3) 
    print(ans)
        
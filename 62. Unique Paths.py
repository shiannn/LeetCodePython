class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        down = m-1
        right = n-1
        A = [[-1]*n for i in range(m)]
        ret = self.uniquePathsutil(down,right,A)
        return ret
    def uniquePathsutil(self,down,right,A):
        print(down,right)
        ans = 0
        if(down == 0 and right == 0):
            return 1
        if(down>0):
            if(A[down-1][right] != -1):
                ans += A[down-1][right]
            else:
                ans += self.uniquePathsutil(down-1,right,A)          
        if(right>0):
            if(A[down][right-1] != -1):
                ans += A[down][right-1]
            else:
                ans += self.uniquePathsutil(down,right-1,A)
        A[down][right] = ans
        return ans
if __name__ == '__main__':
    sol = Solution()
    ans = sol.uniquePaths(23,12)
    print(ans)
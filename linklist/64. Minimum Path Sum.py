class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        if(M == 0):
            return 0
        N = len(grid[0])
        if(N == 0):
            return 0
        ret = [[0]*N for x in range(M)]
        for i in range(M):
            for j in range(N):
                if(i == 0 and j == 0):
                    ret[i][j] = grid[i][j]
                elif(i == 0 and j != 0):
                    ret[i][j] = ret[i][j-1] + grid[i][j]
                elif(i != 0 and j == 0):
                    ret[i][j] = ret[i-1][j] + grid[i][j]
                else:
                    ret[i][j] = min(ret[i-1][j]+grid[i][j],ret[i][j-1]+grid[i][j])
        return ret[M-1][N-1]
if __name__ == '__main__':
    sol = Solution()
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    ans = sol.minPathSum(grid)
    print(ans)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    def minimumTotalutil(self, triangle, idx, N, prev, TempSum):
        if(idx == N):
            print(TempSum)
            global CurrentMin
            if(TempSum < CurrentMin):
                CurrentMin = TempSum
        else:
            if(idx == 0):
                st = [triangle[idx][0]]
            else:
                st = [triangle[idx][prev],triangle[idx][prev+1]]
            for i in range(len(st)):
                num = st[i]
                TempSum += num
                self.minimumTotalutil(triangle, idx+1, N, prev + i, TempSum)
                TempSum -= num
    def minimumTotalutil2(self, triangle, idx, N, prev, TempSum):
        if(idx == N):
            #print(TempSum)
            global CurrentMin
            if(TempSum < CurrentMin):
                CurrentMin = TempSum
        else:
            for i in range(len(triangle[idx])):
                if(i == prev or i == prev+1):
                    num = triangle[idx][i]
                    TempSum += num
                    self.minimumTotalutil(triangle, idx+1, N, i, TempSum)
                    TempSum -= num

if(__name__ == '__main__'):
    sol = Solution()
    T = [
     [-1],
    [2,3],
   [1,-1,-3]
    ]
    ans = sol.minimumTotal(T)
    print(ans)

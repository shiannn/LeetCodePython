class Solution:
    def highestPeak(self, isWater):
        M = len(isWater)
        N = len(isWater[0])
        heightMap = [[-1 for _ in range(N)] for _ in range(M)]
        #print(heightMap)
        que = []
        for m in range(M):
            for n in range(N):
                if isWater[m][n] == 1:
                    heightMap[m][n] = 0
                    que.append((m, n, heightMap[m][n]))
        #print('que', que)
        while(que):
            st = que.pop(0)
            #print(st)
            m, n, h = st
            for dm, dn in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                if m+dm < M and m+dm >= 0 and n+dn<N and n+dn>=0 and heightMap[m+dm][n+dn] == -1:
                    heightMap[m+dm][n+dn] = h+1
                    que.append((m+dm, n+dn, h+1))
        #print(heightMap)
        #print('que', que)

        return heightMap
                

if __name__ == '__main__':
    sol = Solution()
    #isWater = [[0,0,1],[1,0,0],[0,0,0]]
    isWater = [[0,1],[0,0]]
    ret = sol.highestPeak(isWater)
    print(ret)
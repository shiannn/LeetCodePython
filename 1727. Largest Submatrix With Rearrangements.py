class Solution:
    def largestSubmatrix(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        height_matrix = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if i == 0:
                    height_matrix[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        height_matrix[i][j] = matrix[i][j] + height_matrix[i-1][j]
                    else:
                        height_matrix[i][j] = matrix[i][j]
        #print(matrix)
        #print(height_matrix)
        height_matrix = [sorted(row) for row in height_matrix]
        #print(height_matrix)
        ret = 0
        for i in range(M):
            for j in range(N-1, 0-1, -1):
                #print(i, j)
                #print((N-j)*height_matrix[i][j])
                area = (N-j)*height_matrix[i][j]
                ret = max(ret, area)
        return ret

if __name__ == '__main__':
    sol = Solution()
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    #matrix = [[1,0,1,0,1]]
    #matrix = [[0,0],[0,0]]
    ret = sol.largestSubmatrix(matrix)
    print(ret)
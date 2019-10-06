class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        if N == 0:
            return [[]*M]
        for i in range(M):
            for j in range(N):
                if(matrix[i][j] != 0):
                    for m in range(M):
                        if(matrix[m][j] == 0):
                            matrix[i][j] = 'a'
                    for n in range(N):
                        if(matrix[i][n] == 0):
                            matrix[i][j] = 'a'
        for i in range(M):
            for j in range(N):
                if(matrix[i][j] == 'a'):
                    matrix[i][j] = 0
if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
      ]
    sol.setZeroes(matrix)
    print(matrix)
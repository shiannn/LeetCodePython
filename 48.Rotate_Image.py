class Solution(object):
    def rotate(self, matrix):
        #print(matrix)
        self.transpose(matrix)
        #print(matrix)
        self.flip(matrix)
        print(matrix)
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    def transpose(self,matrix):
        M = len(matrix)
        N = len(matrix[0])
        print('M,N',M,N)
        for i in range(M):
            for j in range(i):
                print(i,j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    def flip(self,matrix):
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            for j in range(int(N/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][N-j-1]
                matrix[i][N-j-1] = temp

if __name__ == '__main__':
    """
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    sol = Solution()
    sol.rotate(matrix)
    """
    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]] 
    sol = Solution()
    sol.rotate(matrix)
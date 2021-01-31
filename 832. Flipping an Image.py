class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            #print(A[i])
            for j in range(len(A[0]) // 2):
                temp = A[i][j]
                A[i][j] = A[i][len(A[0]) - 1 - j]
                A[i][len(A[0]) - 1 - j] = temp
            #print(A[i])
            #exit(0)
            for j in range(len(A[0])):
                A[i][j] = 1 - A[i][j]
            #print(A[i])
        
        return A

if __name__ == '__main__':
    sol = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    ret = sol.flipAndInvertImage(A)
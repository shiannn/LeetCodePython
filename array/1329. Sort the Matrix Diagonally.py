from collections import deque

class Solution:
    def diagonalSort(self, mat):
        M = len(mat)
        N = len(mat[0])
        diag = [deque([]) for _ in range(M + N - 1)]
        for i in range(M):
            for j in range(N):
                print(mat[i][j])
                diag[i - j + N - 1].append(mat[i][j])
        #print(diag)
        for i in range(len(diag)):
            diag[i] = deque(sorted(diag[i]))
        #print(diag)
        ret = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M):
            for j in range(N):
                #ret[i][j] = diag[i - j + N - 1].pop(0)
                ret[i][j] = diag[i - j + N - 1].popleft()
        return ret

if __name__ == '__main__':
    sol = Solution()
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    ret = sol.diagonalSort(mat)
    print(ret)
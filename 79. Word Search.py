class Solution:
    def exist(self, board, word):
        M = len(board)
        N = len(board[0])
        #m, n, s = 0, 0, 0
        for m in range(M):
            for n in range(N):
                s = 0
                ret = self.find(board, word, m, n, s)
                if ret:
                    return True
        return False
    
    def find(self, board, word, m, n, s):
        M = len(board)
        N = len(board[0])
        if m < 0 or m >= M or n < 0 or n >= N:
            return False
        if board[m][n] != word[s]:
            return False
        if s == len(word) - 1:
            return True

        tmp = board[m][n]
        board[m][n] = None
        """
        down = self.find(board, word, m+1, n, s+1)
        up = self.find(board, word, m-1, n, s+1)
        right = self.find(board, word, m, n+1, s+1)
        left = self.find(board, word, m, n-1, s+1)
        ret = down or up or right or left
        """
        ret = self.find(board, word, m+1, n, s+1) \
        or self.find(board, word, m-1, n, s+1) \
        or self.find(board, word, m, n+1, s+1) \
        or self.find(board, word, m, n-1, s+1)
        board[m][n] = tmp
        return ret
        

if __name__ == '__main__':
    sol = Solution()
    #board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #word = "ABCCED"
    #board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #word = "SEE"
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    ret = sol.exist(board, word)
    print(ret)
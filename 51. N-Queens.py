class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        already_place = [-1]*n
        ans_list = []
        self.NQueen_util(ans_list,n,0,already_place)
        return ans_list
    def NQueen_util(self,ans_list,n,col,already_place):
        if(col == n):
            self.print_sol(n,already_place,ans_list)
            return
        for i in range(n):
            if(self.is_safe(i,col,already_place) == True):
                already_place[col] = i
                self.NQueen_util(ans_list,n,col+1,already_place)
                already_place[col] = -1
        return
    def is_safe(self,row,col,already_place):
        for i in range(0,col):
            if(already_place[i] == -1):
                continue
            if(already_place[i] == row):
                return False
            if(abs(already_place[i]-row) == abs(i - col)):
                return False
        return True

    def print_sol(self,n,already_place,ans_list):
        sol = ['.'*n for x in range(n)]
        for i in range(n):
            for j in range(n):
                if(already_place[j] == i):
                    #print(sol[i])
                    temp_strlist = list(sol[i])
                    #print(temp_strlist)
                    temp_strlist[j] = 'Q'
                    temp_str = ''.join(temp_strlist)
                    #print('temp_str',temp_str)
                    sol[i] = temp_str
        #print(sol)
        ans_list.append(sol)
if(__name__ == "__main__"):
    sol = Solution()
    ans = sol.solveNQueens(5)
    print(ans)
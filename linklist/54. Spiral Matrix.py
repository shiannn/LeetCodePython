class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = [0,1]
        M = len(matrix)
        if(M==0):
            return []
        N = len(matrix[0])
        done = []
        m=0
        n=0
        temp_M = M
        temp_N = N
        temp_m = 0
        temp_n = 0
        for i in range(M*N):
            print(m,n)
            print(temp_m,temp_M,temp_n,temp_N)
            done.append(matrix[m][n])
            #minus facing
            if(m+direction[0]>=temp_M):
                direction = self.rotate(direction)
                temp_N -= 1
            elif(m+direction[0]<temp_m):
                direction = self.rotate(direction)
                temp_n += 1
            elif(n+direction[1]>=temp_N):
                direction = self.rotate(direction)
                temp_m += 1
            elif(n+direction[1]<temp_n):
                direction = self.rotate(direction)
                temp_M -= 1

            print('dir',direction)
            m+=direction[0]
            n+=direction[1]
            print(m,n)
            print(temp_m,temp_M,temp_n,temp_N)
            print('---')

        return done
    def rotate(self,direction):
        if(direction == [0,1]):
            direction = [1,0]
        elif(direction == [1,0]):
            direction = [0,-1]
        elif(direction == [0,-1]):
            direction = [-1,0]
        elif(direction == [-1,0]):
            direction = [0,1]
        return direction    
if __name__ == "__main__":
    sol = Solution()
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    matrix2 = []
    ans = sol.spiralOrder(matrix2)
    print(ans)
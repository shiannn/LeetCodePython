class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if(n == 0):
            return [0]
        if(n == 1):
            return [0,1]
        else:
            A = self.grayCode(n-1)
            B = A[:]
            B.reverse()
            for i in range(len(B)):
                temp = 1 << int(n-1)
                B[i] += temp
            C = A + B
            return C
if __name__ == '__main__':
    sol = Solution()
    ans = sol.grayCode(4)
    print(ans)
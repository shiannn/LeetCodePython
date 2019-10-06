class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        if(M == 0):
            return False
        N = len(matrix[0])
        if(N == 0):
            return False
        ret = self.BinarySearch(matrix,M,N,target)
        if(ret == -1):
            return False
        else:
            return True

    def BinarySearch(self,nums2D,M,N,target):
        l, r =0, M*N-1
        while(l <= r):
            mid = (l + r)//2
            [row,col] = self.get2DIndex(mid,M,N)
            if(nums2D[row][col] == target):
                return mid
            elif(nums2D[row][col] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1
    def get2DIndex(self,idx,M,N):
        row = idx // N
        col = idx % N
        return [row , col]

if __name__ == '__main__':
    sol = Solution()
    """
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
      ]
    """
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 16
    ret = sol.searchMatrix(matrix,target)
    print(ret)

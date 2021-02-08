class Solution:
    def isMonotonic(self, A):
        isup = self.isincreasing(A)
        isdown = self.isincreasing([-a for a in A])
        return (isup or isdown)
    def isincreasing(self, A):
        if len(A) <= 1:
            return True
        prev = A[0]
        for a in A[1:]:
            if a < prev:
                return False
            prev = a
        return True

if __name__ == '__main__':
    sol = Solution()
    #A = [1,2,2,3]
    #A = [6,5,4,4]
    #A = [1,3,2]
    #A = [1,2,4,5]
    A = [1,1,1]
    ret = sol.isMonotonic(A)
    print(ret)
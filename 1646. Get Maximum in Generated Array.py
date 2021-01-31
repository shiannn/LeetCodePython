class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [-1]* (n+1)
        nums[0] = 0
        nums[1] = 1
        maxi = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
            if nums[i] > maxi:
                maxi = nums[i]
        #print(nums)
        return maxi

if __name__ == '__main__':
    sol = Solution()
    n = 7
    ret = sol.getMaximumGenerated(n)
    print(ret)
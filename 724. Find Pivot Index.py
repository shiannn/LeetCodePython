class Solution:
    def pivotIndex(self, nums) -> int:
        sums = []
        sum_ = 0
        for num in nums:
            sum_ += num
            sums.append(sum_)
        #print(sums)
        N = len(nums)
        for i in range(N):
            if i == 0:
                lsum = 0
                rsum = sums[N-1]-sums[i]
                #print(lsum, rsum)
            elif i == N-1:
                lsum = sums[N-2]
                rsum = 0
                #print(lsum, rsum)
            else:
                lsum = sums[i-1]
                rsum = sums[N-1]-sums[i]
                #print(i, lsum, rsum)
            if lsum == rsum:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    #nums = [1,7,3,6,5,6]
    #nums = [1,2,3]
    #nums = [2,1,-1]
    nums = [5]
    ret = sol.pivotIndex(nums)
    print(ret)
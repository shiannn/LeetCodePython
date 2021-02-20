class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        A = {0:-1}
        sum_ = 0
        for idx, num in enumerate(nums):
            sum_ += num
            toFind = sum_ if k==0 else sum_ % k
            if toFind in A:
                if idx - A[toFind] > 1:
                    return True
            else:
                A[toFind] = idx
        return False

if __name__ == '__main__':
    sol = Solution()
    #nums = [6,6]
    #nums = [23, 2, 4, 6, 7]
    #nums = [23, 23, 23, 23, 23, 23]
    #nums = [23, 23, 23]
    nums = [23, -23, 23]
    k=0
    ret = sol.checkSubarraySum(nums, k)
    print(ret)
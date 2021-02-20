class Solution:
    def subarraySum(self, nums, k) -> int:
        sum_ = 0
        A = {0:1}
        ret = 0
        for num in nums:
            sum_ += num
            ret += 0 if (sum_-k) not in A else A[sum_-k]
            if sum_ not in A:
                A[sum_] = 1
            else:
                A[sum_] += 1
            #print(A)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [1,1,1]
    #k = 2
    nums = [1,2,3]
    k = 3
    ret = sol.subarraySum(nums, k)
    print(ret)
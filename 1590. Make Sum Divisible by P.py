class Solution:
    def minSubarray(self, nums, p: int) -> int:
        ### Find a short subarray same mod p as sum(p)
        if sum(nums) < p:
            return -1
        elif sum(nums) == p:
            return 0
        remain = sum(nums) % p
        if remain == 0:
            return 0
        sum_ = 0
        A = {0:-1}
        ret = float('inf')
        for idx, num in enumerate(nums):
            sum_ += num
            if ((sum_ - remain)% p) in A:
                ret = min(ret, idx - A[((sum_ - remain)% p)])
            A[sum_ % p] = idx
            #print(idx, ret)
        if ret == len(nums) or ret == float('inf'):
            return -1
        else:
            return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [3,1,4,2]
    #p = 6
    #nums = [6,3,5,2]
    #p = 9
    #nums = [1,2,3]
    #p = 3
    #nums = [1,2,3]
    #p = 7
    #nums = [1000000000,1000000000,1000000000]
    #p = 3
    nums = [4,4,2]
    p = 7
    ret = sol.minSubarray(nums, p)
    print(ret)
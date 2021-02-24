class Solution:
    def minOperations(self, nums, x: int) -> int:
        N = len(nums)
        if sum(nums) < x:
            return -1
        elif sum(nums) == x:
            return N
        l = 0
        target_sum = sum(nums) - x
        #print('target_sum', target_sum)
        sum_ = 0
        A = {0:-1}
        ret = -1
        for idx, num in enumerate(nums):
            sum_ += num
            #print(idx, sum_ - target_sum)
            if sum_ - target_sum in A:
                #print(idx - A[sum_ - target_sum])
                ret = max(idx - A[sum_ - target_sum], ret)
            if sum_ not in A:
                A[sum_] = idx
            #print(idx, ret)
        return (N - ret) if ret != -1 else -1

if __name__ == '__main__':
    sol = Solution()
    #nums = [1,1,4,2,3]
    #x = 5
    #nums = [5,6,7,8,9]
    #x = 4
    #nums = [3,2,20,1,1,3]
    #x = 10
    nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
    x = 134365
    ret = sol.minOperations(nums, x)
    print(ret)
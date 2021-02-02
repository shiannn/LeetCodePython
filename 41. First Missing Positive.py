import time

class Solution:
    def firstMissingPositive(self, nums):
        N = len(nums)
        for i in range(N):
            print(i)
            while(nums[i]-1 != i and nums[i] > 0 and nums[i] <= N and nums[nums[i]-1]!=nums[i]):
                ### swap nums[i] to its position nums[i]-1
                src, tgt = i, nums[i]-1
                temp = nums[src]
                #print('temp', temp)
                nums[src] = nums[tgt]
                nums[tgt] = temp
                #time.sleep(1)
            print(nums)
        for i in range(N):
            if nums[i] != (i+1):
                return i+1
        
        return N+1

if __name__ == '__main__':
    sol = Solution()
    #nums = [3,4,-1,1]
    #nums = [1,2,0]
    nums = [7,8,9,11,12]
    ret = sol.firstMissingPositive(nums)
    print(ret)
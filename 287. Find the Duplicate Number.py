class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val] < 0:
                return val
            else:
                nums[val] = -nums[val]
        #print(nums)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,4,2,2]
    #nums = [3,1,3,4,2]
    #nums = [1,1]
    #nums = [1,1,2]
    ret = sol.findDuplicate(nums)
    print(ret)
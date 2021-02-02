class Solution:
    def findErrorNums(self, nums):
        errors = []
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                errors.append(val)
            else:
                nums[val - 1] *= -1
        #print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                errors.append(i+1)
        return errors

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2,4]
    ret = sol.findErrorNums(nums)
    print(ret)
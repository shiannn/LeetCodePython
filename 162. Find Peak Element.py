import math

class Solution:
    def findPeakElement(self, nums):
        nums.insert(0, -math.inf)
        nums.append(-math.inf)
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1
        #print(nums)
        
if __name__ == '__main__':
    sol = Solution()
    #nums = [1,2,3,1]
    nums = [1,2,1,3,5,6,4]
    ret = sol.findPeakElement(nums)
    print(ret)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        NumZeros = 0
        NumOnes = 0
        NumTwos = 0
        for num in nums:
            if(num == 0):
                NumZeros+=1
            if(num == 1):
                NumOnes+=1
            if(num == 2):
                NumTwos+=1
        print(NumZeros,NumOnes,NumTwos)
        for i in range(0,NumZeros):
            nums[i] = 0
        for i in range(NumZeros,NumZeros+NumOnes):
            nums[i] = 1
        for i in range(NumZeros+NumOnes,NumZeros+NumOnes+NumTwos):
            nums[i] = 2
        print(nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
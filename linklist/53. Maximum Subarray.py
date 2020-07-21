import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cum = self.cumulative(nums)
        N = len(cum)
        sub_array = []
        largest_sum = -sys.maxsize-1
        for i in range(N):
            for j in range(i,N):
                if(cum[j]-cum[i]+nums[i]>largest_sum):
                    largest_sum = cum[j]-cum[i]+nums[i]
                    sub_array = nums[i:j+1]
        #print(sub_array)
        return largest_sum

    def cumulative(self, nums):
        N = len(nums)
        cumul = [0]*N
        cumul[0] = nums[0]
        for i in range(1,N):
            cumul[i] = cumul[i-1] + nums[i]
        #print(cumul)
        return cumul

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,6,7]
    #sol.cumulative(nums)
    ans = sol.maxSubArray([1])
    print(ans)
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = -sys.maxsize-1
        for num in nums:
            if (current_sum>0):
                current_sum += num
            else:
                current_sum = num
            if(current_sum>max_sum):
                max_sum = current_sum
        return max_sum
if(__name__ == "__main__"):
    sol = Solution()
    A = [-2,1,-3,4,-1,2,1,-5,4]
    ans = sol.maxSubArray(A)
    print(ans)
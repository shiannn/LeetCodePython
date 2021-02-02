class Solution:
    def singleNumber(self, nums):
        ret = 0
        for num in nums:
            ret ^= num
        
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [4,1,2,1,2]
    nums = [2,2,1]
    ret = sol.singleNumber(nums)
    print(ret)
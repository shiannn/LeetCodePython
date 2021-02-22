class Solution:
    def check(self, nums) -> bool:
        num_decrease = 0
        for idx, num in enumerate(nums):
            if num < nums[(idx-1)%len(nums)]:
                num_decrease += 1
        if num_decrease <= 1:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    #nums = [3,4,5,1,2]
    #nums = [2,1,3,4]
    #nums = [1,2,3]
    #nums = [1,1,1]
    nums = [2,1]
    ret = sol.check(nums)
    print(ret)
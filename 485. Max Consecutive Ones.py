class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ret = 0
        temp = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                temp += 1
                if i == len(nums) - 1:
                    if temp > ret:
                        ret = temp
            else:
                if temp > ret:
                    ret = temp
                temp = 0
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [1,1,0,1,1,1]
    nums = [1, 1, 1, 1, 0, 1,1,1,1,1,1]
    ret = sol.findMaxConsecutiveOnes(nums)
    print(ret)
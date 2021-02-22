class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 0:
            return 0
        maxs = [nums[0]]
        mins = [nums[0]]
        ret = nums[0]
        for idx, num in enumerate(nums[1:], 1):
            #print(idx, num)
            max_ = max(num, maxs[idx-1]* num, mins[idx-1]* num)
            min_ = min(num, maxs[idx-1]* num, mins[idx-1]* num)
            ret = max(ret, max_)
            maxs.append(max_)
            mins.append(min_)
            #print('maxs', maxs)
            #print('mins', mins)
            #print('ret', ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [2,3,-2,4]
    nums = [-2,0,-1]
    ret = sol.maxProduct(nums)
    print(ret)
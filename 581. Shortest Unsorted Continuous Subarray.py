class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        end = -2
        start = -1
        max_ = -float('inf')
        for idx, num in enumerate(nums):
            max_ = max(max_, num)
            if max_ != num:
                end = idx
        min_ = float('inf')
        for idx, num in reversed(list(enumerate(nums))):
            #print(idx, num)
            min_ = min(min_, num)
            if min_ != num:
                start = idx
        #print(start, end)
        return end - start + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [2,6,4,8,10,9,15]
    ret = sol.findUnsortedSubarray(nums)
    print(ret)
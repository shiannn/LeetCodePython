class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums == []):
            return 0
        nums.append('a')
        count = 1
        SameFlag = False
        i = 1
        while(nums[i] != 'a'):
            if nums[i] == nums[i-1]:
                if(SameFlag == False):
                    SameFlag = True
                    count += 1
                    i += 1
                else:
                    del nums[i]
            else:
                SameFlag = False
                count += 1
                i += 1
        del nums[-1]
        return count
if __name__ == '__main__':
    sol = Solution()
    #nums = [1,1,1,2,2,3]
    #nums = [0,0,1,1,1,1,2,3,3]
    #nums = []
    nums = [1]
    ans = sol.removeDuplicates(nums)
    print(ans)
    print(nums)
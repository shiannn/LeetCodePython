class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return None
        ThreeList = [nums[0], nums[1], nums[2]]
        ThreeList = sorted(ThreeList)
        TwoList = [nums[0], nums[1]]
        TwoList = sorted(TwoList)
        TwoList.reverse()
        for i in range(3,len(nums)):
            if(nums[i]>ThreeList[2]):
                ThreeList[0] = ThreeList[1]
                ThreeList[1] = ThreeList[2]
                ThreeList[2] = nums[i]
            elif(nums[i]>ThreeList[1]):
                ThreeList[0] = ThreeList[1]
                ThreeList[1] = nums[i]
            elif(nums[i]>ThreeList[0]):
                ThreeList[0] = nums[i]
            else:
                pass

        for i in range(2,len(nums)):
            if(nums[i]<TwoList[1]):
                TwoList[0] = TwoList[1]
                TwoList[1] = nums[i]
            elif(nums[i]<TwoList[0]):
                TwoList[0] = nums[i]
            else:
                pass
        return max(ThreeList[0]*ThreeList[1]*ThreeList[2],max(ThreeList)*TwoList[0]*TwoList[1])

if __name__=='__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    ans = sol.maximumProduct(nums)
    print(ans)
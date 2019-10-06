class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        layer = len(nums)
        nums.sort()
        TempGet = []
        OverallGet = []
        self.subsetsWithDuputil(nums,layer,0,TempGet,OverallGet)
        return OverallGet
    
    def subsetsWithDuputil(self,nums,layer,idx,TempGet,OverallGet):
        if(idx == layer):
            toput = TempGet[:]
            OverallGet.append(toput)
        else:
            number = nums.count(nums[idx])
            print('number',number)
            for i in range(number+1):
                TempGet.extend(nums[idx:idx+i])
                A = TempGet
                self.subsetsWithDuputil(nums,layer,idx+number,TempGet,OverallGet)
                TempGet = TempGet[:len(TempGet)-i]

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2]
    ans = sol.subsetsWithDup(nums)
    print(ans)
    print(len(ans))
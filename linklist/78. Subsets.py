class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Overall = []
        SubList = []
        nums = list(set(nums))
        N = len(nums)
        self.subsetsutil(Overall,SubList,nums,0,N)
        return Overall
    
    def subsetsutil(self,Overall,SubList,nums,idx,N):
        if(idx == N):
            to_append = SubList[:]
            Overall.append(to_append)
            print('Sublist',SubList)
            #print('b','idx',idx,'Sublist',SubList,'Overall',Overall)
        else:
            self.subsetsutil(Overall,SubList,nums,idx+1,N)
            SubList.append(nums[idx])
            self.subsetsutil(Overall,SubList,nums,idx+1,N)
            SubList.pop()

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,2,3]
    ans = sol.subsets(nums)
    print(ans)
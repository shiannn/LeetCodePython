class Solution:
    def canChoose(self, groups, nums) -> bool:
        st = 0
        for group in groups:
            #print(st, group)
            while(st <= (len(nums)-len(group)) and not self.ismatch(group, nums[st:st+len(group)])):
                #print(st, group, nums[st:st+len(group)], self.ismatch(group, nums[st:st+len(group)]))
                st += 1
            ### match st print(st)
            if st > (len(nums)-len(group)):
                return False
            else:
                st = st + len(group)
        return True
                
    def ismatch(self, one, two):
        for g, n in zip(one, two):
            if g!=n:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    groups = [[1,-1,-1],[3,-2,0]]
    nums = [1,-1,0,1,-1,-1,3,-2,0]
    #groups = [[10,-2],[1,2,3,4]]
    #nums = [1,2,3,4,10,-2]
    #groups = [[1,2,3],[3,4]]
    #nums = [7,7,1,2,3,4,7,7]
    ret = sol.canChoose(groups, nums)
    print(ret)
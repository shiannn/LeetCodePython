class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = range(pow(2,n))
        N = len(nums)
        ans = self.grayCodeutil(nums,N,-1,0,[])
        return ans
    def grayCodeutil(self,nums,N,prev,idx,current):
        #print('idx',idx)
        if(idx == N):
            #print(current)
            if(self.safe(current,N)):
                print(current,'good')
                return current 
        for i in range(0,N):
            if(nums[i] not in current):
                current.append(nums[i]) 
                AnsList = self.grayCodeutil(nums,N,i,idx+1,current)
                if(AnsList!=None):
                    return AnsList
                current.pop()
    def safe(self,current,N):
        for i in range(1,N):
            if (self.PowerTwo(current[i]^current[i-1])==False):
                return False
        return True
    def PowerTwo(self,a):
        if(a == 0):
            return False
        while(a%2==0):
            a/=2
        if(a==1):
            return True
        else:
            return False
if __name__ == '__main__':
    sol = Solution()
    ans = sol.grayCode(4)    
    print(ans)
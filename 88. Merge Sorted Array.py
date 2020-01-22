class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ret = [0]*(m+n)
        c1=0
        c2=0
        for i in range(m+n):
            if(c1>=m):
                ret[i] = nums2[c2]
                c2+=1
            elif(c2>=n):
                ret[i] = nums1[c1]
                c1+=1
            else:
                if(nums1[c1]<nums2[c2]):
                    ret[i] = nums1[c1]
                    c1+=1
                else:
                    ret[i] = nums2[c2]
                    c2+=1
        #return ret
        for i in range(m+n):
            nums1[i] = ret[i]

if __name__=="__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    ans = sol.merge(nums1,m,nums2,n)
    print(nums1)
class Solution:
    def maxNumber(self, nums1, nums2, k):
        ret = None
        for i in range(0, k+1):
            digits1 = self.getMaxdigits(nums1, i)
            digits2 = self.getMaxdigits(nums2, k-i)
            digits = self.merge(digits1, digits2)
            #ret = digits if ret is None else self.larger(digits, ret)
            if len(digits) != k:
                continue
            ret = digits if ret is None else max(digits, ret)
            #print(digits1, digits2, digits, ret)
        return ret
    """
    def larger(self, As, Bs):
        if len(As) == len(Bs):
            for a, b in zip(As, Bs):
                if a > b:
                    return As
                elif a < b:
                    return Bs
            return As
        else:
            return As if (len(As) > len(Bs)) else Bs
    """

    def getMaxdigits(self, nums, k):
        ret = []
        for i in range(len(nums)):
            #print(ret, nums[i])
            tail = len(ret) - 1
            ### currently (tail+1) in ret
            while(tail >= 0 and ret[tail] < nums[i] and len(nums)-i>k-len(ret)):
                ret.pop()
                tail = tail - 1
            ret.append(nums[i])
        return ret[:k]
    
    def merge(self, digits1, digits2):
        ret = []
        dptr1, dptr2 = 0, 0
        while(dptr1 != len(digits1) and dptr2 != len(digits2)):
            if digits1[dptr1] > digits2[dptr2]:
                ret.append(digits1[dptr1])
                dptr1+=1
            elif digits1[dptr1] < digits2[dptr2]:
                ret.append(digits2[dptr2])
                dptr2+=1
            else:
                if digits1[dptr1:] > digits2[dptr2:]:
                    ret.append(digits1[dptr1])
                    dptr1+=1
                else:
                    ret.append(digits2[dptr2])
                    dptr2+=1
        while(dptr1 != len(digits1)):
            ret.append(digits1[dptr1])
            dptr1+=1
        while(dptr2 != len(digits2)):
            ret.append(digits2[dptr2])
            dptr2+=1
        
        return ret

if __name__ == '__main__':
    sol = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    #nums1 = [6,7]
    #nums2 = [6,0,4]
    #k = 5
    ret = sol.maxNumber(nums1, nums2, k)
    print(ret)
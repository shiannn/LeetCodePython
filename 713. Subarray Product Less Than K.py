class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        l, r = 0, 0
        cur_product = 1
        ret = 0
        while(r<len(nums)):
            cur_product *= nums[r]
            ### cur_product is PI[l, r]
            while(l<=r and cur_product >= k):
                cur_product /= nums[l]
                l += 1
            ### cur_product is PI[l, r]
            ret += (r-l+1)
            r += 1
        return ret
        
if __name__ == '__main__':
    sol = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    ret = sol.numSubarrayProductLessThanK(nums, k)
    print(ret)
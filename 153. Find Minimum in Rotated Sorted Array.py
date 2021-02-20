class Solution:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        l = 0
        r = N-1
        while(l <= r):
            mid = l + (r-l) // 2
            if (nums[(mid+1)%N] > nums[mid]) and (nums[(mid-1)%N] > nums[mid]):
                return nums[mid]
            elif nums[mid] > nums[r]:
                ### abandon left
                l = mid + 1
            elif nums[mid] < nums[r]:
                ### abandon right
                r = mid - 1


if __name__ == '__main__':
    sol = Solution()
    #nums = [3,4,5,1,2]
    #nums = [4,5,6,7,0,1,2]
    nums = [11,13,15,17]
    ret = sol.findMin(nums)
    print(ret)
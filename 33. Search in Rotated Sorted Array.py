class Solution:
    def search(self, nums, target):
        right = len(nums) - 1
        left = 0
        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            ### decide which interval to abort
            elif nums[mid] > nums[right]:
                ### left is sorted
                if not (target >= nums[left] and target <= nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                ### right is sorted
                if not (target <= nums[right] and target >= nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                    

if __name__ == '__main__':
    sol = Solution()
    #nums = [4,5,6,7,0,1,2]
    #target = 0
    #nums = [4,5,6,7,0,1,2]
    #target = 3
    nums = [1]
    target = 0
    ret = sol.search(nums, target)
    print(ret)
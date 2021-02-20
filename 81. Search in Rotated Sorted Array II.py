class Solution:
    def search(self, nums, target):
        right = len(nums) - 1
        left = 0
        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            ### decide which interval to abort
            elif nums[mid] > nums[right]:
                ### left is sorted
                if not (target >= nums[left] and target <= nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < nums[right]:
                ### right is sorted
                if not (target <= nums[right] and target >= nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                ### mid equals right
                ### shrink the search interval since right is not the solution
                right -= 1
        return False
                    

if __name__ == '__main__':
    sol = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    ret = sol.search(nums, target)
    print(ret)
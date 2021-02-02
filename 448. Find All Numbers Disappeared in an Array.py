class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]

        disappears = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappears.append(i + 1)
        print(disappears)
        return disappears


if __name__ == '__main__':
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    sol.findDisappearedNumbers(nums)
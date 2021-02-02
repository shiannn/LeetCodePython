class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        start = 0
        finished = 0
        while(finished != N):
            left = nums[start]
            idx = (start + k) % N
            while(idx != start):
                ### swap with left
                temp = nums[idx]
                nums[idx] = left
                left = temp
                finished += 1
                idx = (idx + k) % N
            temp = nums[idx]
            nums[idx] = left
            left = temp
            finished += 1
            start += 1
        print(nums)
        
if __name__ == '__main__':
    sol = Solution()
    #nums = [1,2,3,4,5,6,7]
    #k = 3
    nums = [-1,-100,3,99]
    k = 2
    sol.rotate(nums, k)
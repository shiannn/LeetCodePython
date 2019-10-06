class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = [[]]
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        for i in range(index, len(nums)):
            print(path + [nums[i]])
            res.append(path + [nums[i]])
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for x in nums:
            with_x = []
            for s in result:
                with_x.append(s + [x])
            print('x',x,'with_x',with_x)
            result = result + with_x
        return result
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    #sol.subsets(nums)
    sol.subsets2(nums)
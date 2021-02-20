class Solution:
    def longestConsecutive(self, nums):
        S = set({})
        for num in nums:
            S.add(num)
        print(S)
        ret = 0
        for num in nums:
            if num in S:
                pre = num - 1
                nxt = num + 1
                while pre in S:
                    S.remove(pre)
                    pre -= 1
                while nxt in S:
                    S.remove(nxt)
                    nxt += 1
                span = nxt - 1 - pre
                if span > ret:
                    ret = span
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    ret = sol.longestConsecutive(nums)
    print(ret)
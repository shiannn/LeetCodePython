class Solution:
    def shuffle(self, nums, n: int):
        i, j = 0, n
        ret = []
        while(i != n):
            ret.append(nums[i])
            ret.append(nums[j])
            i+=1
            j+=1
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [2,5,1,3,4,7]
    #n = 3
    #nums = [1,2,3,4,4,3,2,1]
    #n = 4
    nums = [1,1,2,2]
    n = 2
    ret = sol.shuffle(nums, n)
    print(ret)
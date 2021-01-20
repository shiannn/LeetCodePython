class Solution:
    def canJump(self, nums) -> bool:
        ret = self.check_idx(nums, 0)
        return ret

    def check_idx(self, nums, idx):
        #print(idx)
        if idx == len(nums) - 1:
            return True
        if idx >= len(nums):
            return False
        maxi = -1
        chosen = -1
        for i in range(1, nums[idx]+1):
            next_idx = idx + i
            print(next_idx)
            if next_idx == len(nums) - 1:
                return True

            if nums[next_idx] + next_idx >= maxi:
                chosen = next_idx
                maxi = nums[next_idx] + next_idx
        if chosen == -1:
            return False
        ret = self.check_idx(nums, chosen)
        return ret
        """
        try:
            self.check_idx(nums, chosen)
        except:
            print('a')
        """

class Solution2:
    def canJump(self, nums) -> bool:
        dp_table = [-1]* len(nums)
        ret = self.check_idx(nums, 0, dp_table)
        return ret

    def check_idx(self, nums, idx, dp_table):
        if idx == (len(nums) - 1):
            return True
        elif idx > (len(nums) - 1):
            return False
        else:
            if dp_table[idx] == True:
                return True
            elif dp_table[idx] == False:
                return False
            else:
                ret = False
                cur_idx = idx
                #for num in range(1, nums[cur_idx]+1):
                for num in range(nums[cur_idx], 0, -1):
                    #print(num)
                    sub_ret = self.check_idx(nums, cur_idx + num, dp_table)
                    ret = (ret or sub_ret)
                    if ret == True:
                        break

                dp_table[cur_idx] = ret
                return ret

def main():
    nums = [2,3,1,1,4]
    #nums = [3,2,1,0,4]
    sol = Solution()
    ret = sol.canJump(nums)
    print(ret)

if __name__ == '__main__':
    main()
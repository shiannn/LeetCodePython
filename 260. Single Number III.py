class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        self.getBits(xor)
        split = None
        for i in range(32):
            if((1 << i) & xor) > 0:
                split = (1 << i)
        print(split)
        left = 0
        right = 0
        for num in nums:
            if (split & num) == 0:
                left ^= num
            else:
                right ^= num
        print(left, right)
        return [left, right]
    
    def getBits(self, number):
        ret = ""
        for _ in range(5):
            ret = str(number % 2) + ret
            number = number // 2
        print(ret)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,1,3,2,5]
    ret = sol.singleNumber(nums)
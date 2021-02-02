class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ### If twos is 1, then ones should always be 0
            #new_ones = (num ^ ones) & ~twos
            ### If ones is 1, then ones would then be (num ^ ones)
            ### If ones is 0, then ones would then be [if twos 1, ones is 0], [if twos 0, ones is num ^ ones]

            new_ones = (ones & (num ^ ones)) | (~ones & ((twos & 0) | (~twos & num ^ ones)))
            ### If twos is 1, then twos becomes twos ^ num
            ### If twos is 0, then twos becomes num & ones
            twos = (twos & (twos ^ num)) | (~twos & (num & ones))
            ones = new_ones
            #print(num, self.getBits(ones), self.getBits(twos))
        print(ones)
        return ones
    
    def getBits(self, number):
        ret = ""
        for i in range(5):
            ret = str(number % 2) + ret
            number = number // 2
        return ret

if __name__ == '__main__':
    sol = Solution()
    #nums = [2,2,3,2]
    nums = [0,1,0,1,0,1,99]
    sol.singleNumber(nums)
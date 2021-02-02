class Solution:
    def findTheDifference1(self, s, t):
        ori_sum = 0
        for tt in t:
            ori_sum += ord(tt)
        for ss in s:
            ori_sum -= ord(ss)
        #print(chr(ori_sum))
        return chr(ori_sum)
    
    def findTheDifference2(self, s, t):
        record = 0
        for ss in s:
            record ^= ord(ss)
        for tt in t:
            record ^= ord(tt)
            """
            if tt not in already:
                return tt
            else:
                already.remove(tt)
            """
        return chr(record)
    
    def findTheDifference(self, s, t):
        already = {}
        for ss in s:
            if ss not in already:
                already[ss] = 1
            else:
                already[ss] += 1
        for tt in t:
            #print(tt, already[tt])
            if tt not in already or already[tt] == 0:
                return tt
            else:
                already[tt] -= 1


if __name__ == '__main__':
    sol = Solution()
    s = "abcd"
    t = "abcde"
    ret = sol.findTheDifference(s, t)
    print(ret)
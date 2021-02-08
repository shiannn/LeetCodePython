class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        difference = []
        cumsum = []
        for ss, tt in zip(s, t):
            #print(abs(ord(ss) - ord(tt)))
            difference.append(abs(ord(ss) - ord(tt)))
        print(difference)
        temp = 0
        for d in difference:
            cumsum.append(temp + d)
            temp += d
        print(cumsum)
        cur_max = 0
        for i in range(len(cumsum)):
            ### only check the position which is possible to be longer substrings
            for j in range(i+cur_max, len(cumsum)):
                ### close intervals [i, j]
                #print(i, j)
                sumi2j = cumsum[j] - cumsum[i] + difference[i]
                print('sum{}to{}'.format(i, j), sumi2j)
                if sumi2j <= maxCost:
                    cur_max = max(cur_max, j - i + 1)
                else:
                    break
        #print('cur_max', cur_max)
        return cur_max


if  __name__ == '__main__':
    sol = Solution()
    """
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    """
    """
    s = "abcd"
    t = "cdef"
    maxCost = 3
    """
    s = "abcd"
    t = "acde"
    maxCost = 0
    ret = sol.equalSubstring(s, t, maxCost)
    print(ret)
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N = len(s)
        mapFreq = {}
        for i in range(0, N - minSize + 1, 1):
            already = set({})
            for j in range(i, i+minSize):
                already.add(s[j])
            if len(already) <= maxLetters:
                if s[i:i+minSize] not in mapFreq:
                    #print('word', s[i:i+minSize])
                    mapFreq[s[i:i+minSize]] = 1
                else:
                    mapFreq[s[i:i+minSize]] += 1
            #print(mapFreq)
        if len(mapFreq) == 0:
            ret = 0
        else:
            ret = max([mapFreq[word] for word in mapFreq])
        #print(ret)
        return ret


if __name__ == '__main__':
    sol = Solution()
    """
    s = "aababcaab"
    maxLetters = 2
    minSize = 3
    maxSize = 4
    """
    """
    s = "aaaa"
    maxLetters = 1
    minSize = 3
    maxSize = 3
    """
    """
    s = "aabcabcab"
    maxLetters = 2
    minSize = 2
    maxSize = 3
    """
    s = "abcde"
    maxLetters = 2
    minSize = 3
    maxSize = 3
    ret = sol.maxFreq(s, maxLetters, minSize, maxSize)
    print(ret)
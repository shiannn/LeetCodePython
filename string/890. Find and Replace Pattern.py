class Solution:
    def findAndReplacePattern(self, words, pattern):
        ret = []
        pattern_num = self.getNumbers(pattern)
        #print(pattern_num)
        for word in words:
            word_num = self.getNumbers(word)
            if pattern_num == word_num:
                ret.append(word)
        return ret
    
    def getNumbers(self, word):
        s, cur = {}, 0
        num = ""
        for c in word:
            if c not in s:
                s[c] = str(cur)
                cur += 1
            num += s[c]
        #print(word, num)
        return num
            

if __name__ == '__main__':
    sol = Solution()
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    ret = sol.findAndReplacePattern(words, pattern)
    print(ret)
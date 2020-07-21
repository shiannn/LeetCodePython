class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        s = str.strip()
        if len(s) == 0:
            return 0
        flag = 1
        if s[0] == '+':
            s = s[1:]
            flag = 1
        elif s[0] == '-':
            s = s[1:]
            flag = -1
        retNum = 0
        for c in s:
            if c >= '0' and c <= '9':
                retNum *= 10
                retNum += (ord(c) - ord('0'))
            else:
                break

        retNum *= flag
        if retNum >= 2147483647:
            retNum = 2147483647
        elif retNum <= -2147483648:
            retNum = -2147483648
        
        return retNum
        
if __name__ == '__main__':
    sol = Solution()
    #s = "   4193 with words"
    s = " "
    ret = sol.myAtoi(s)
    print(ret)
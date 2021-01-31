class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        bit = 0
        ret = ""
        all_len = max(len(a), len(b))
        for i in range(1, all_len+1):
            if len(a) - i >= 0:
                aa = a[len(a) - i]
            else:
                aa = 0
            if len(b) - i >= 0:
                bb = b[len(b) - i]
            else:
                bb = 0

            bit = int(aa) + int(bb) + carry
            if bit == 0:
                ret = "0"+ret
                carry = 0
            elif bit == 1:
                ret = "1"+ret
                carry = 0
            elif bit == 2:
                ret = "0"+ret
                carry = 1
            elif bit == 3:
                ret = "1"+ret
                carry = 1
        if carry > 0:
            ret = str(carry) + ret
        return ret
            

if __name__ == '__main__':
    #a = '11'
    #b = '1'
    a = "1010"
    b = "1011"
    sol = Solution()
    ret = sol.addBinary(a, b)
    print(ret)
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400,100, 90,50 ,40 ,10 ,9 ,5,4, 1]
        position =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ret = ""
        for v, pos in zip(val, position):
            while(num >= v):
                ret += pos
                num -= v
        return ret

if __name__ == '__main__':
    sol = Solution()
    ret = sol.intToRoman(1994)
    print(ret)
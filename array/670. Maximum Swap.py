class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = num
        digits = []
        while(temp > 0):
            digits.insert(0, temp % 10)
            temp = temp // 10
        print(digits)
        for i in range(len(digits)):
            max_value = -1
            max_index = -1
            for j in range(i, len(digits)):
                if digits[j] >= max_value:
                    max_value = digits[j]
                    max_index = j
                #print('j, max_value', j, max_value)
            if max_value != digits[i]:
                ### swap i & j
                temp = digits[i]
                digits[i] = digits[max_index]
                digits[max_index] = temp
                break
        print(digits)
        ret = 0
        for digit in digits:
            ret = ret*10 + digit
        return ret

if __name__ == '__main__':
    sol = Solution()
    num = 2736
    num = 9973
    ret = sol.maximumSwap(num)
    print(ret)
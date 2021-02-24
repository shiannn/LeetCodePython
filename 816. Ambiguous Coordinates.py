class Solution:
    def ambiguousCoordinates(self, S: str):
        digits = S[1:-1]
        ret = []
        for idx in range(1, len(digits)):
            #print(idx, digits[:idx], digits[idx:])
            dec_l = self.count_decimal_points(digits[:idx])
            dec_r = self.count_decimal_points(digits[idx:])
            #print(dec_l, dec_r)
            for dl in dec_l:
                for dr in dec_r:
                    ret.append('({}, {})'.format(dl, dr))

            #print(ret)
        return ret

    def count_decimal_points(self, sub_digits):
        if len(sub_digits) == 1:
            return set({sub_digits})
        else:
            ### length >= 2
            if sub_digits[0] == '0' and sub_digits[-1] == '0':
                return set({})
            elif sub_digits[0] != '0' and sub_digits[-1] != '0':
                with_point = set(
                    {sub_digits[:idx] + '.' + sub_digits[idx:] for idx in range(1, len(sub_digits))}
                )
                without_point = set({sub_digits})
                ret = with_point | without_point

                return ret 
            elif sub_digits[0] == '0' and sub_digits[-1] != '0':
                return set({sub_digits[0] + '.' + sub_digits[1:]})
            elif sub_digits[0] != '0' and sub_digits[-1] == '0':
                return set({sub_digits})

if __name__ == '__main__':
    sol = Solution()
    #S = "(123)"
    #S = "(00011)"
    #S = "(0123)"
    S = "(100)"
    ret = sol.ambiguousCoordinates(S)
    print(ret)
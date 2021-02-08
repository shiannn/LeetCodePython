class Solution:
    def canMakePaliQueries(self, s: str, queries):
        prefix_nums = []
        temp = {chr(j): 0 for j in range(ord('a'), ord('a') + 26)}
        #print(temp)
        for i in range(len(s)):
            """
            for j in range(ord('a'), ord('a') + 26):
                print(chr(j))
                temp[chr(j)] = 0
            """
            temp[s[i]] += 1
            prefix_nums.append(temp.copy())
        #print(prefix_nums)
        ret = []
        for query in queries:
            s, t, k = query
            need = 0
            for j in range(ord('a'), ord('a')+26):
                if s > 0:
                    num_char = prefix_nums[t][chr(j)] - prefix_nums[s-1][chr(j)]
                else:
                    num_char = prefix_nums[t][chr(j)]
                #print('diff', diff['a'])
                if num_char % 2 == 0:
                    pass
                else:
                    need += 1
            required = need // 2
            #print(required)
            if required <= k:
                ret.append(True)
            else:
                ret.append(False)
        return ret


if __name__ == '__main__':
    sol = Solution()
    s = "abcda"
    queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
    ret = sol.canMakePaliQueries(s, queries)
    print(ret)
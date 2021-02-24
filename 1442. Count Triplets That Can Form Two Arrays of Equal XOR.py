class Solution:
    def countTriplets(self, arr) -> int:
        xors = []
        xor_ = 0
        A = {0:1}
        sum_ = {0:0}
        ret = 0
        for i in range(len(arr)):
            xor_ ^= arr[i]
            if xor_ in A:
                pseudo_leng = A[xor_]* (i+1)
                pseudo_leng -= sum_[xor_]
                ### each occurence of xor=0 should minus 1 for num_split (a, b)
                ret += pseudo_leng - A[xor_]* 1
            if xor_ in sum_:
                sum_[xor_] += (i+1)
            else:
                sum_[xor_] = (i+1)
            if xor_ in A:
                A[xor_] += 1
            else:
                A[xor_] = 1
            #print(A, ret)
        return ret

    def countTriplets1(self, arr) -> int:
        xors = []
        xor_ = 0
        for i in range(len(arr)):
            xor_ ^= arr[i]
            xors.append(xor_)
        #print(xors)
        ret = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    #print(i,j,k)
                    ### [i, j), [j, k]
                    if i >= 1:
                        a = xors[j-1] ^ xors[i-1]
                    else:
                        a = xors[j-1]
                    b = xors[k] ^ xors[j-1]
                    #print('a b', a, b)
                    if a == b:
                        ret += 1
        return ret

if __name__ == '__main__':
    sol = Solution()
    #arr = [2,3,1,6,7]
    #arr = [1,1,1,1,1]
    #arr = [2,3]
    #arr = [1,3,5,7,9]
    arr = [7,11,12,9,5,2,7,17,22]
    ret = sol.countTriplets(arr)
    print(ret)
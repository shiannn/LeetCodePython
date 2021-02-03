class Solution:
    def pancakeSort(self, arr):
        ret = []
        N = len(arr)
        for i in range(N, 0, -1):
            #print(arr, i)
            pos_i = self.getElement(arr, i)
            self.pancakeFlip(arr, pos_i+1)
            #print(arr, i)
            ret.append(pos_i+1)
            self.pancakeFlip(arr, i)
            ret.append(i)
        return ret
    
    def getElement(self, arr, n):
        for i in range(len(arr)):
            if arr[i] == n:
                return i

    def pancakeFlip(self, arr, k):
        #N = len(arr)
        for i in range(k // 2):
            temp = arr[i]
            arr[i] = arr[k - 1 - i]
            arr[k - 1 - i] = temp

if __name__ == '__main__':
    sol = Solution()
    #arr = [3,2,4,1]
    arr = [1,2,3]
    ret = sol.pancakeSort(arr)
    print(ret)
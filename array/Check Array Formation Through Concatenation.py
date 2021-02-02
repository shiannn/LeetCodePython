class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        cur = 0
        while(cur != len(arr)):
            found = False
            for piece in pieces:
                if arr[cur] in piece:
                    found = True
                    if not(arr[cur:cur+len(piece)] == piece):
                        return False
                    else:
                        cur += len(piece)
                        break
                else:
                    found = False
            if found == False:
                return False

        return True

if __name__ == '__main__':
    sol = Solution()
    #arr = [15,88]
    #pieces = [[88],[15]]
    #arr = [49,18,16]
    #pieces = [[16,18,49]]
    #arr = [91,4,64,78]
    #pieces = [[78],[4,64],[91]]
    arr = [1,3,5,7]
    pieces = [[2,4,6,8]]
    ret = sol.canFormArray(arr, pieces)
    print(ret)
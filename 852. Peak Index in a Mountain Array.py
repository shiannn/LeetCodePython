class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        N = len(arr)
        l = 0
        r = N-1
        while(l <= r):
            mid = l + (r - l) // 2
            if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                return mid
            elif(arr[mid] > arr[mid - 1]) and (arr[mid] < arr[mid + 1]):
                ### abandon left
                l = mid
            elif(arr[mid] < arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                ### abandon right
                r = mid

if __name__ == '__main__':
    sol = Solution()
    arr = [0,1,0]
    #arr = [0,2,1,0]
    #arr = [0,10,5,2]
    #arr = [3,4,5,1]
    #arr = [24,69,100,99,79,78,67,36,26,19]
    ret = sol.peakIndexInMountainArray(arr)
    print(ret)
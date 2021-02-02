class Solution:
    def maxArea(self, height):
        maxi = -1
        l, r = 0, len(height) - 1
        while(l < r):
            if (r - l)* min(height[l], height[r]) > maxi:
                maxi = (r - l)* min(height[l], height[r])
            #print(l, r, (r - l)* min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxi

if __name__ == '__main__':
    #height = [4,3,2,1,4]
    #height = [1,2,1]
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    ret = sol.maxArea(height)
    print(ret)
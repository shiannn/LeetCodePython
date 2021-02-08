class Solution:
    def numTeams(self, rating):
        N = len(rating)
        left = [0]*N
        right = [0]*N
        for i in range(N):
            ### fill in the left[i], right[i]
            for j in range(i):
                left[i] += (rating[j] < rating[i])
            for j in range(i+1, N):
                right[i] += (rating[j] > rating[i])
        #print(rating)
        #print(left)
        #print(right)
        ret = 0
        for i in range(N):
            increasing = left[i]* right[i]
            decreasing = (i-left[i])* (N-(i+1)-right[i])
            #print('increasing, decreasing', increasing, decreasing)
            ret += (increasing + decreasing)
        #print(ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #rating = [2,5,3,4,1]
    rating = [2,1,3]
    #rating = [1,2,3,4]
    ret = sol.numTeams(rating)
    print(ret)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ret = []
        for interval in intervals:
            #print(ret,interval)
            if(ret == []):
                ret.append(interval)
            elif(interval[0]<=ret[-1][1]<=interval[1]):
                ret[-1][1] = interval[1]
            elif(ret[-1][1]<interval[0]):
                ret.append(interval)
        return ret
if(__name__ == '__main__'):
    sol = Solution()
    #testinput =  [[1,3],[2,6],[8,10],[15,18]]
    testinput = [[1,4],[4,5]]
    ans = sol.merge(testinput)
    print(ans)
class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        ret = []
        cur = 0
        while(cur < len(intervals) and intervals[cur][1] < newInterval[0]):
            ret.append(intervals[cur])
            cur += 1
        ### cur is overlap with newInterval
        toInsert_s = newInterval[0]
        toInsert_t = newInterval[1]
        ### find toInsert_t
        print(toInsert_s)
        while(cur < len(intervals) and intervals[cur][0] <= newInterval[1]):
            toInsert_s = min(intervals[cur][0], toInsert_s)
            toInsert_t = max(intervals[cur][1], toInsert_t)
            cur += 1
        print(toInsert_t)
        ret.append([toInsert_s, toInsert_t])
        while(cur < len(intervals)):
            ret.append(intervals[cur])
            cur += 1
        print(ret)
        return ret

if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    sol = Solution()
    sol.insert(intervals, newInterval)
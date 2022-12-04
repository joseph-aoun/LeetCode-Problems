class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        ans = 0
        start = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= start[1]:
                start = intervals[i]
            else:
                ans += 1
        
        
        return ans
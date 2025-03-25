class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        curr_start, curr_end = 0, 0
        res = 0

        for i in range(len(meetings)):
            if meetings[i][0] > curr_end:
                res += meetings[i][0] - curr_end - 1
                curr_start = meetings[i][0]
                curr_end = meetings[i][1]
            else:
                curr_end = max(curr_end, meetings[i][1])

        return res + days - curr_end
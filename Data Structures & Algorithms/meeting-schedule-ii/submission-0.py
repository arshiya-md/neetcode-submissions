"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Minimum number of rooms required to schedule all meetings without any conflicts means
# if there is no conflict one room is enough
# 1 conflict -> 2 rooms
# 2 conflicts -> 3 rooms
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        st = et = 0

        res = count = 0

        while st < len(intervals):
            if start_times[st] < end_times[et]:
                st += 1
                count += 1
            else:
                et += 1
                count -= 1

            res = max(res, count)

        return res


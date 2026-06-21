"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)

        for idx in range(1, len(intervals)):

            if intervals[idx].start < intervals[idx-1].end:
                return False
                
        return True


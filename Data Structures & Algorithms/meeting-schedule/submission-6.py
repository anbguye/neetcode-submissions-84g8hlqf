"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda pair: pair.start)
        prevEnd = intervals[0].end

        for curr in intervals[1:]:

            if curr.start < prevEnd:
                return False
            else:
                prevEnd = curr.end
        
        return True


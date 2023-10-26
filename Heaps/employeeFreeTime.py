#https://leetcode.com/problems/employee-free-time/

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # sort intervals.
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
                
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        
        # merge overlapping intervals.
        merged_intervals = []
        
        for start,end in intervals:
            if merged_intervals and  start <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])

            else:   
                merged_intervals.append([start,end])
                
        # check of free slots.
        free_slots = []
        
        for i in range(1, len(merged_intervals)):
            gap_start = merged_intervals[i-1][1]
            gap_end = merged_intervals[i][0]
            free_slots.append(Interval(start=gap_start, end=gap_end))
            
        return free_slots

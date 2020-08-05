# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if(len(intervals)==0):
            return 0
        if(len(intervals)==1):
            return 1
        intervals = sorted(intervals, key=lambda x:x[0])
        rooms = [intervals[0]]
        count = 1
        brflag = False
        for i in range(1,len(intervals)):
            # print("rooms = {}".format(rooms))
            brflag = False
            if(len(rooms)==0):
                rooms.append(intervals[i])
            else:
                s = intervals[i][0]
                e = intervals[i][1]
                for r in rooms:
                    if(s>=r[1]):
                        rooms.remove(r)
                        rooms.append(intervals[i])
                        brflag = True
                        break
                if(brflag==False):
                    rooms.append(intervals[i])
                    count += 1
                
        return count
                    
                
            
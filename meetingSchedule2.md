Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.
Example 1:
Input:
[[0, 30],[5, 10],[15, 20]]
Output:
 2
Example 2:
Input:
 [[7,10],[2,4]]

Output:
 1


```
import heapq

def mRoomsTwo(schedule):
    if schedule:
        schedule.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, (schedule[0][1], schedule[0]))
        ans = 1
        for i in range(1, len(schedule)):
            meeting = schedule[i] #[15, 20]
            done = False
            while not done:
                if rooms:
                    inProgMeeting = heapq.heappop(rooms) #(30, [0, 30])
                    if inProgMeeting[0] > meeting[0]:
                        heapq.heappush(rooms, inProgMeeting)
                        heapq.heappush(rooms, (meeting[1], meeting))
                        done = True
                    ans = max(ans, len(rooms))
                else:
                    done = True
                    heapq.heappush(rooms, (meeting[1], meeting))

        return ans
    return 0

print(mRoomsTwo([[2,4], [7,10]]))
```

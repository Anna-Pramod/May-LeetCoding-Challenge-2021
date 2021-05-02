#There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

#You will start on the 1st day and you cannot take two or more courses simultaneously.

#Return the maximum number of courses that you can take.

#Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
#Output: 3
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        # first task is to sort the last_day 
        courses.sort(key = lambda x: x[1])
        
        #add the duration to the max_heap
        max_heap = []
        time = 0
        for duration,last_day in courses:
            heappush(max_heap, -duration)   #since this is a max_heap push -duration
            time = time + duration
            if time > last_day:             #check the condition
                taken = heappop(max_heap)
                time = time + taken
                
        return (len(max_heap))
     
        # time complexity would probably be O(nlog(n)) and space complexity would probably be O(n)
      
# 97 / 97 test cases passed.
# Status: Accepted
# Runtime: 708 ms
# Memory Usage: 19.4 MB

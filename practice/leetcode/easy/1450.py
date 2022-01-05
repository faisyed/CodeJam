class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        return len([st for st, en in zip(startTime, endTime) if st <= queryTime <= en])

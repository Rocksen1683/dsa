class MyCalendar:

    def __init__(self):
        self.times = []

    def book(self, startTime: int, endTime: int) -> bool:
        for sT, eT in self.times: 
            if sT < endTime and startTime < eT:
                return False
        
        #add the time 
        self.times.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
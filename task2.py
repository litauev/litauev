class DateTime():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
 
    def display(self):
        print(f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')
 
time_1 = DateTime(14, 1, 5)
time_1.display()
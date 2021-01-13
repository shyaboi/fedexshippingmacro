from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

toDay = datetime.today().weekday()

def switch(today):
    if today == 0:
        today = 'Monday'
        print(today)
        return
    if today == 1:
        today = 'Tuesday'
        print(today)
        return 
    if today == 2:
        today = 'Wednesday'
        print(today)
        return
    if today == 3:
        today = 'Thursday'
        print(today)
        return
    if today == 4:
        today = 'Friday'
        print(today)
        return
    if today == 5:
        today = 'Saturday'
        print(today)
        return
    if today == 6:
        today = 'Sunday'
        print(today)
        return
    else:
        print('not a day')

        
switch(toDay)
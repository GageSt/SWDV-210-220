#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    #start_time = datetime.now("%H/%M:/%S")
    #start_time_string = start_time.strftime(start_time[12:]) #[Error: datetime.datetime object not subscriptable]
    print(f"Start time:, {start_time:%X.%f}") #formatted string needed to display start_time pg.309 X = time formatted for locale f = microsecond
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()   
    print(f"Stop time: , {stop_time:%X.%f}")
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if days > 0:
        print(f"Hours/minutes: {time_object:%H:%M}") #Where H is Hours and M is Minute
    print(f"Seconds: {time_object:%S.%f}")           #Where S os Second and f is microseconds

if __name__ == "__main__":
    main()

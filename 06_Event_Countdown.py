# Event Countdown Timer
from datetime import datetime, timedelta
import time

# Step-1: Get Event Date and Time from user
def get_event_datetime():
    try:
        date_input = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Please enter again.")
        return None

# Step-2: Calculating Time Remaining
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

# Step-3: Display Countdown
def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\rTime remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")

# Step-4: Main Countdown Loop
def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\nCountdown Complete!")
            break
        display_countdown(time_left)
        time.sleep(1)

# Main program loop
event_datetime = get_event_datetime()
if event_datetime:
    print(f"Event set for: {event_datetime}")
    start_countdown(event_datetime)


# Learnings

#1. get_event_datetime()
# Accepts user input for event date & time
# Converts the input string into a datetime object (strptime)
# Ensures correct format is entered

#2.calculate_time_remaining(event_date)
# Compares current time (datetime.now()) with event time
# Returns the difference as a timedelta object

#3.display_countdown(time_left)
# Extracts days, hours, minutes, and seconds from timedelta
# Uses divmod() for neat breakdown of seconds
# Prints formatted countdown in real time

#4.start_countdown(event_date)
# Runs a loop to continuously update countdown
# Stops when time is up (total_seconds() <= 0)
# Uses time.sleep(1) for 1-second delay → real ticking effect

#5.datetime.now()
# Fetches the current system date & time at execution moment

#6.divmod(x, y)
# Efficiently returns quotient & remainder in one step
# Handy for splitting seconds into hours, minutes, seconds

#7.time.sleep(1)
# Pauses program execution for 1 second
# Ensures countdown updates in real time

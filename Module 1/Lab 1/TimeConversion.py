# Convert time format
# You have been given a time in the 12-hour AM/PM format. Your task is to convert the given time into military (24-hour) format.
# 
# Please note the following conversion rules:
# 12:00:00 AM on a 12-hour clock is equivalent to 00:00:00 on a 24-hour clock.
# 12:00:00 PM on a 12-hour clock is equivalent to 12:00:00 on a 24-hour clock.
# Apply the following steps to convert the time format:
# Analyze the given time in the 12-hour AM/PM format.
# If the time is before noon (AM), leave it as is unless it is exactly 12:00:00 AM, which needs to be converted to 00:00:00 in the 24-hour format.
# If the time is in the afternoon (PM), add 12 hours to the hour component of the time, except when it is exactly 12:00:00 PM, which remains the same in the 24-hour format.
# Represent the converted time in the military (24-hour) format.
# 
# Important Note:
# Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# input:
# 12:13:04PM
# output:
# 24:13:04
# Exercise-2
# 
# input:
# 12:07:09AM
# output:
# 00:07:09
# Exercise-3
# 
# input:
# 02:07:09AM
# output:
# 02:07:09

# Solution:-

#Import Necessary Libraries
import sys

def convert_to_24_hour_format(time_str):
    # Split the time string into hours, minutes, and seconds
    time_components = time_str[:-2].split(':')
    hours, minutes, seconds = map(int, time_components)
    
    # Check if it's PM and not 12:00:00 PM, then add 12 hours
    if "PM" in time_str:
        hours += 12
    # Check if it's AM and 12:00:00 AM, then set hours to 0
    elif "AM" in time_str and hours == 12:
        hours = 0
    
    # Format the output in 24-hour format
    military_time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    
    return military_time_str

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = convert_to_24_hour_format(inputVal)

#Print Output
print(outputVal)
# Finding the average of number series:
# To find the average of a number series, you need to add up all the numbers in the series and then divide the sum by the total number of values in the series.
# 
# Here's an example:
# Let's say we have the number series: 5, 10, 15, 20, 25.
# 
# To find the average, we add up all the numbers: 5 + 10 + 15 + 20 + 25 = 75.
# 
# Next, we divide the sum by the total number of values in the series, which is 5 in this case (since there are 5 numbers in the series).
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Average = 75 / 5 = 15.
# 
# Exercise-1
# 
# input:
# 1 2 3 4 5
# output:
# 3
# Exercise-2
# 
# input:
# 2 2 2 2 -2
# output:
# 2

# Solution:-

#Import Necessary Libraries
import sys

def calculate_average(series):
    # Convert the input series of strings to a list of integers
    numbers = list(map(int, series.split()))

    # Calculate the sum of the numbers in the series
    total_sum = sum(numbers)

    # Calculate the average by dividing the sum by the total number of values
    average = total_sum / len(numbers)

    # Return the calculated average
    return round(average)

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = calculate_average(inputVal)

#Print Output
print(outputVal)
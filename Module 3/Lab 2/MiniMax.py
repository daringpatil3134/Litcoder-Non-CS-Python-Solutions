# Get possible min and max values on summing 4 of 6 numbers.
# You are provided with six positive integers. Your objective is to determine the minimum and maximum values that can be obtained by summing exactly four out of the six integers. Print the resulting minimum and maximum values on a single line, separated by a space, as two long integers.
# 
# To achieve this, follow these steps:
# 
# Take any four numbers from the given set of six positive integers and calculate their sum.
# Repeat this process for all possible combinations of four numbers.
# Identify the smallest sum as the minimum value and the largest sum as the maximum value.
# Print the calculated minimum and maximum values, ensuring they are represented as long integers and separated by a space.
# 
# **Important Note: **
# Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# input:
# 1 3 4 2 5 6
# output:
# 10 18
# Exercise-2
# 
# input:
# 12 3 4 8 1 5
# output:
# 13 29

# Solution:-

#Import Necessary Libraries
import sys

def min_max_sums(nums):
    # Sort the list of numbers in ascending order
    sorted_nums = sorted(nums)

    # Calculate the minimum sum by considering the first four numbers
    min_sum = sum(sorted_nums[:4])

    # Calculate the maximum sum by considering the last four numbers
    max_sum = sum(sorted_nums[2:])

    return min_sum, max_sum

#Take Input
inputVal = list(map(int, input().split()))

#Process Output Using Function
minVal, maxVal = min_max_sums(inputVal)

#Print Output
print(minVal, maxVal)
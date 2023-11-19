# Frequency Count of Each Element
# You are currently engaged in a data analysis project that involves one specific task: determining the frequency count of each element within a given array. This task is essential for your data analysis project. Please write a code to find the frequency count of each element.
# Example:
# If you are giving input 1 3 2 4 5 4
# Step 1 : Arrange the elements in ascending order - 1 2 3 4 4 5
# 
# The frequency of given number 0-0, 1-1, 2-1, 3-1, 4-2, 5-1
# So the output is 0 1 1 1 2 1
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# input:
# 8
# 1 3 4 5 4 3 6 2
# output:
# 0 1 1 2 2 1 1
# 
# Exercise-2
# input:
# 6
# 7 3 8 5 7 3
# output:
# 0 0 0 2 0 1 0 2 1

# Solution:-

#Import Necessary Libraries
import sys

def frequency_count(arr, n):
    # Max Value in Array
    maxVal = max(arr) + 1

    # Initialize array to store the frequency count
    count_list = [0] * maxVal

    # Iterate through the array to fill frequency count
    for i in range (n):
        # read number at i index of arr
        val = arr[i]
        # increment count of number
        count_list[val] += 1

    # Create Result String
    result_str = ' '.join(map(str, count_list))
    
    # Return Output
    return result_str

#Take Input
inputNum = int(input())
arrInput = list(map(int, input().split()))

# Call the function with user input
outputVal = frequency_count(arrInput, inputNum)

#Print Output
print(outputVal)
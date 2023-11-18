# Sort Colors
# How can an array named "nums" containing objects labeled as "Crimson," "Ivory," or "Azure," or objects representing colors (0, 1, or 2), be sorted in-place, such that objects of the same color or label are adjacent, and the colors or labels appear in the specific order of crimson, ivory, and azure?
# 
# For example, consider the input array [2, 0, 1] or ['Azure', 'Crimson', 'Ivory']. The desired output would be [0, 1, 2] or ['Crimson', 'Ivory', 'Azure'], respectively, where all the 0s or 'Crimson' objects are grouped together, followed by all the 1s or 'Ivory' objects , and finally, all the 2s or 'Azure' objects.
# 
# Important Note:
# Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input :
# 1 2 1 2 0 1 2 0
# 
# Output :
# 0 0 1 1 1 2 2 2
# 
# Exercise-2
# 
# Input:
# 2 2 2 1 1 1 1 0 0 0
# 
# Output:
# 0 0 0 1 1 1 1 2 2 2

# Solution:-

#Import Necessary Libraries
import sys

def sort_colors(input_str):
    # Convert the input string to a list of integers
    nums = list(map(int, input_str.split()))

    # Count the occurrences of each color
    count = [0] * 3

    # Count the occurrences of each color in the input array
    for num in nums:
        count[num] += 1

    # Update the input array based on the counts
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[index] = color
            index += 1

    # Convert the sorted array to a string with spaces
    sorted_str = ' '.join(map(str, nums))

    return sorted_str

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = sort_colors(inputVal)

#Print Output
print(outputVal)
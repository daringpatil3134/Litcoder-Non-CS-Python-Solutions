# Jump Game:
# You are given an integer array nums, where each element in the array represents your maximum jump length at that position. Initially, you are positioned at the first index (index 0) of the array.
# 
# Your objective is to determine whether it is possible to reach the last index (index nums.length - 1) of the array following these rules:
# 
# Starting from the first index, you can make jumps to other indices based on the value at each index. For example, if nums[0] is 3, you can jump to indices 1, 2, or 3.
# 
# The maximum number of steps you can take from any given index is limited by the value at that index in the nums array.
# 
# Your goal is to reach the last index using the minimum number of jumps possible.
# 
# Return true if you can successfully reach the last index, or false if it is not possible to do so.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input :
# 3 2 4 0 0 7
# 
# Note:
# line 1 : input array value
# 
# Output :
# true
# 
# Exercise-2
# 
# Input:
# 3 2 1 0 0 7
# 
# Output:
# false

# Solution:-

#Import Necessary Libraries
import sys

def can_jump(nums):
    max_reach = 0
    target = len(nums) - 1

    for i in range(len(nums)):
        # If the current index is beyond the maximum reach, it's not possible
        # to reach the end
        if i > max_reach:
            return "false"

        # Update the maximum reachable index
        max_reach = max(max_reach, i + nums[i])

        # If the maximum reachable index is beyond or equal to the target,
        # return True
        if max_reach >= target:
            return "true"

    return "false"

# Take input from the console
nums_input = list(map(int, input().split()))

# Call the function with user input
result = can_jump(nums_input)
print(result)
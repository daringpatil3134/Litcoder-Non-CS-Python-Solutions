# Closest Triples
# Given an integer array nums of length n and an integer target, you need to find three integers in the nums array such that their sum is closest to the target. Your task is to implement a function that returns the sum of the three integers.
# 
# Return the sum of the three integers.
# 
# Example:
# 
# INPUT
# [-1, 2, 1, -4]
# 1
# OUTPUT
# 2
# 
# Exercise-1
# 
# Input :
# 1 2 3 4
# 1
# 
# Output :
# 6

# Solution:-

#Import Necessary Libraries
import sys

def threeSumClosest(nums_str, target_str):
    nums = list(map(int, nums_str.split()))
    target = int(target_str)
    
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum

    return closest_sum

#Take Input
inputarr = input()
inputtarget = input()

#Process Output Using Function
outputVal = threeSumClosest(inputarr, inputtarget)

#Print Output
print(outputVal)
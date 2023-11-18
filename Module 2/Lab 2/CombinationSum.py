# Combination Sum:
# Given a distinct array of integers called "candidates" and a target integer called "target," your task is to find and return a list of all unique combinations of numbers from the candidates array, where the chosen numbers sum up to the target. You can use any number from the candidates array an unlimited number of times in each combination. Two combinations are considered unique if they differ in the frequency of at least one chosen number.
# 
# Example:
# 
# Input:
# Candidates: [2, 3, 5]
# Target: 8
# 
# Output:
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input :
# 2 3 4 5
# 
# 8
# 
# Output :
# 2 2 2 2
# 2 2 4
# 2 3 3
# 3 5
# 4 4
# 
# Exercise-2
# 
# Input:
# 2 3 4 5
# 
# 4
# Output:
# 2 2
# 4

# Solution:-

#Import Necessary Libraries
import sys

def combination_sum(candidates, target):
    def backtrack(start, path, current_sum):
        if current_sum == target:
            combinations.append(path[:])
            return
        if current_sum > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, current_sum + candidates[i])
            path.pop()

    combinations = []
    candidates.sort()
    backtrack(0, [], 0)
    return combinations

# Take input from the console
candidates_input = input()
temp = input()
target_input = int(input())

# Convert input strings to lists of integers
candidates_list = list(map(int, candidates_input.split()))

#Process Output Using Function
outputVal = combination_sum(candidates_list, target_input)

# Print combinations on new lines
for combination in outputVal:
    print(" ".join(map(str, combination)))
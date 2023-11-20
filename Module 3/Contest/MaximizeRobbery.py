# Maximize Robbery
# The task is to find the maximum amount of money a thief can rob from a row of houses. Each house contains a certain amount of money. However, the thief has a rule that they cannot rob two adjacent houses. We need to determine the maximum amount of money the thief can steal while following this constraint.
# 
# For example, let's consider a row of houses with the following amounts of money: [100, 200, 150, 50, 300]. The thief needs to find the best strategy to maximize their stolen amount.
# 
# The thief cannot rob adjacent houses. Therefore, they have two options at each house: either rob the current house and move two houses ahead or skip the current house and move to the next house.
# 
# To maximize the stolen amount, the thief should consider the maximum amount of money they can steal at each step. By calculating the maximum amount of money that can be robbed for each house, the thief can determine the overall maximum stolen amount.
# 
# The task is to implement an algorithm that finds the maximum amount of money the thief can rob from the given row of houses while following the constraint of not robbing adjacent houses.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# Input:
# 1 2 3 4 5 6
# Output:
# 12
# 
# Exercise-2
# Input:
# 1 2 3 4 5 6 7
# Output:
# 16

# Solution:-

#Import Necessary Libraries
import sys

def max_robbery_amount(houses):
    n = len(houses)
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return houses[0]
    elif n == 2:
        return max(houses[0], houses[1])

    # Initialize an array to store the maximum stolen amount up to each house
    dp = [0] * n

    # Base cases for the first two houses
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    # Iterate over the rest of the houses to calculate the maximum stolen amount
    for i in range(2, n):
        # Choose the maximum between robbing the current house and skipping it
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    # Return the maximum stolen amount from the last house
    return dp[-1]

#Take Input
inputVal = input()

#Conver Input String into Array
input = list(map(int, inputVal.split()))

#Process Output Using Function
outputVal = max_robbery_amount(input)

#Print Output
print(outputVal)
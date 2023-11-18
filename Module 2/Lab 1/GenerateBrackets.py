# Generate Brackets:
# You are given an integer n, which represents the number of pairs of parentheses. You need to write a function that generates all possible combinations of well-formed parentheses using n pairs.
# 
# Suppose n = 2. We need to generate all combinations of well-formed parentheses using 2 pairs of parentheses.
# 
# The possible combinations are ['(())', '()()'].
# 
# The first combination is (()), where the inner parentheses are well-formed.
# The second combination is ()(), where both pairs of parentheses are well-formed.
# 
# Thus, the expected output is ['(())', '()()'].
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# Input :
# 2
# 
# Output :
# (()),()()
# 
# Exercise-2
# Input:
# 3
# 
# Output:
# ((())),(()()),(())(),()(()),()()()

# Solution:-

#Import Necessary Libraries
import sys

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)

    # Convert the array to a string with spaces
    result_str = ','.join(map(str, result))

    return result_str

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = generate_parentheses(int(inputVal))

#Print Output
print(outputVal)
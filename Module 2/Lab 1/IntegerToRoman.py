# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. For example, 2 is written as II in Roman numerals, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Example
# 
# INPUT
# III
# 
# OUTPUT
# 3
# 
# Exercise-1
# 
# Input :
# LXI
# 
# Output :
# 61
# 
# Exercise-2
# 
# Input:
# MXI
# 
# Output:
# 1011

# Solution:-

#Import Necessary Libraries
import sys

def roman_to_int(roman_str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    prev_value = 0
    for numeral in reversed(roman_str):
        current_value = roman_dict[numeral]

        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value

        prev_value = current_value

    return result

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = roman_to_int(inputVal)

#Print Output
print(outputVal)
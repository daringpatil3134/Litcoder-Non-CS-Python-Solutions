# Reverse a string
# Imagine you are a software engineer working on a text processing application. Your task is to develop a function that reverses a given string while preserving the position of punctuation marks, spaces, and the case of the letters. This function will be used to process input from users and provide them with the reversed string as an output.
# 
# Example :
# Input: "No lemon, no melon"
# Output: "no lemon, no meloN"
# 
# Input: "Race car"
# Output: "race caR"
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input:
# Litcoder is best
# 
# Output:
# tsebsire do ctiL
# Exercise-2
# 
# Input:
# i like Litcoder
# 
# Output:
# r edoc tiLekili

# Solution:-

#Import Necessary Libraries
import sys

def reverse_string_with_preservation(input_str):
    # Separate the string into words
    words = input_str.split()

    # Reverse each word while preserving punctuation and case
    reversed_words = []
    for word in words:
        # Separate letters and punctuation
        letters = [char for char in word if char.isalpha()]
        punctuation = [char for char in word if not char.isalpha()]

        # Reverse letters and combine with punctuation
        reversed_word = ''.join(letters[::-1]) + ''.join(punctuation)
        reversed_words.append(reversed_word)

    # Join the reversed words into the final result
    result = ' '.join(reversed_words)
    return result

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = reverse_string_with_preservation(inputVal)

#Print Output
print(outputVal)
# Letter Tile Possibilities
# You are given a collection of tiles, where each tile has a single letter printed on it. The objective is to find out how many different non-empty sequences of letters can be formed using the given tiles. A sequence is considered non-empty if it contains at least one letter.
# 
# Example Scenario:
# 
# Let's consider the following scenario as an example:
# 
# Input:
# 
# Tiles: "AAB"
# 
# Explanation:
# 
# In this scenario, we have three tiles with letters "A," "A," and "B" printed on them.
# 
# Now, we need to find all possible distinct non-empty sequences of letters that can be formed using these tiles.
# 
# Possible sequences:
# 
# "A"
# "AA"
# "AAB"
# "AB"
# "BA"
# "B"
# "AA"
# "ABA"
# 
# There are 8 different non-empty sequences that can be formed using the given tiles "AAB".
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input : 
# FFG
# 
# Output :
# 8
# Exercise-2
# 
# Input:
# FFGHJ
# 
# Output:
# 170

# Solution:-

#Import Necessary Libraries
import sys
from itertools import permutations

def numTilePossibilities(tiles):
    # Initialize a counter for the number of possibilities
    count = 0
    # Convert the input string into a list of characters
    a = list(tiles)
    # Iterate over all possible lengths of subsequences
    for i in range(1, len(tiles) + 1):
        # Generate all permutations of length 'i' from the list of characters
        per = permutations(a, i)
        # Convert the permutations to a set to remove duplicates
        s = set(per)
        # Iterate over unique permutations and increment the count
        for item in s:
            count += 1
    # Return the total count of possibilities
    return count

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = numTilePossibilities(inputVal)

#Print Output
print(outputVal)
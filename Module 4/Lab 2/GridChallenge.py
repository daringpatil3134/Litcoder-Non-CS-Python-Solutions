# Grid Challenge
# You are provided with a square grid of characters consisting of lowercase ASCII letters (a-z). Your task is to rearrange the elements in each row in ascending alphabetical order. After that, you need to determine if the columns are also arranged in ascending alphabetical order from top to bottom. If the columns meet this criterion, you should return "YES"; otherwise, return "NO".
# 
# For example, consider the grid ['pqr','stu','vxy']. In this case, the rows are already sorted alphabetically. Additionally, the columns 'p q r', 's t u', and 'v x y' are also in alphabetical order. Therefore, the answer would be "YES".
# It's important to note that elements can only be rearranged within the same row and cannot be moved to a different row.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# input:
# 1,3 3,abc,def,ghi
# output:
# YES
# 
# Here ,
# 1 - is number of record
# 3 3 - is grid size
# abc,def,ghi - input characters
# 
# Exercise-2
# input:
# 1,3 3,ibc,def,ghi
# output:
# NO
# 
# Exercise-3
# input:
# 1,3 3,abc,ief,ghi
# output:
# YES

# Solution:-

# Import Necessary Libraries
import sys

def is_grid_sorted(rows, cols, grid_chars):
    # Parse the input
    grid = [list(grid_chars[i:i+cols]) for i in range(0, len(grid_chars), cols)]

    # Sort each row
    sorted_grid = [''.join(sorted(row)) for row in grid]

    # Check if columns are sorted
    transposed_grid = list(zip(*sorted_grid))
    if all(''.join(col) == ''.join(sorted(col)) for col in transposed_grid):
        return "YES"
    else:
        return "NO"

# Take Input
record, grid_size, *characters = input().split(",")
rows, cols = map(int, grid_size.split())

# Process Output Using Function
result = is_grid_sorted(rows, cols, ''.join(characters))

# Print Output
print(result)
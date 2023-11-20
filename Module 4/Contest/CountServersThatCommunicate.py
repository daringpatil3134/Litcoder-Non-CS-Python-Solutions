# Count Servers that Communicate
# In a server center represented as an m x n integer matrix grid, each cell contains either a server (denoted by 1) or no server (denoted by 0). Servers on the same row or column are considered to be communicating with each other.
# You need to determine the total count of servers that communicate with at least one other server.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input : 
# 4
# 1 0 1 1
# 0 0 0 0
# 0 1 0 0
# 0 0 0 1
# 
# Note:
# First line : number of row 
# Rest of the lines: m x n matrics
# 
# Output :
# 4
# Exercise-2
# 
# Input:
# 4
# 1 0 0 1
# 0 0 1 0
# 0 1 0 0
# 0 0 0 1
# 
# Output:
# 3

# Solution:-

#Import Necessary Libraries
import sys

def count_communicating_servers(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Lists to store the count of servers in each row and column
    row_counts = [0] * rows
    col_counts = [0] * cols

    # Count the number of servers in each row and column
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_counts[i] += 1
                col_counts[j] += 1

    # Count the total number of servers that communicate with at least one other server
    total_communicating_servers = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                total_communicating_servers += 1

    # Return the total count of communicating servers
    return total_communicating_servers

#Take Input
inputRows = int(input())
inputMatrix = [list(map(int, input().split())) for _ in range(inputRows)]

#Process Output Using Function
outputVal = count_communicating_servers(inputMatrix)

#Print Output
print(outputVal)
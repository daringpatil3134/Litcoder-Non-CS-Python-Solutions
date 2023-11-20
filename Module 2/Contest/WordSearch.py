# Word Search in Grid
# You are given an m x n grid of characters and a target word. Your task is to determine whether the word exists in the grid.
# 
# The word can be formed by using letters from sequentially adjacent cells, where adjacent cells are those that are horizontally or vertically neighboring. Each letter cell can only be used once in the word.
# 
# Example:
# 
# INPUT
# 3
# 4
# SEE
# A B C E
# S F C S
# A D E E
# 
# OUTPUT
# Yes
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# 
# Input :
# 
# 4
# 
# 4
# good
# agcd eooh ijdl rfgt
# 
# Note :
# line 1 : row value
# Line 2 : column value
# Line 3 : input string
# Line 4 : string array
# 
# Output :
# Yes
# 
# Exercise-2
# 
# Input:
# 4
# 
# 4
# truth
# tgcd ruoh ityl rhit
# 
# Output:
# Yes

# Solution:-

#Import Necessary Libraries
import sys

def exist(board, word):
    def dfs(i, j, k):
        if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        temp, board[i][j] = board[i][j], '/'
        res = (
            dfs(i + 1, j, k + 1) or
            dfs(i - 1, j, k + 1) or
            dfs(i, j + 1, k + 1) or
            dfs(i, j - 1, k + 1)
        )
        board[i][j] = temp
        return res

    if not board or not board[0]:
        return "No"

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return "Yes"
    return "No"

# Take input from the console
row = int(input())
col = int(input())
word = input()
grid = [list(input().split()) for _ in range(row)]

# Call the function with user input
result = exist(grid, word)
print(result)
# Tower Breakers
# Tower Breakers is a game played between two players, where the first move is always made by Player 1. The game revolves around a set of towers with varying heights. Each tower has a height represented by the value m, and there are initially n towers.
# 
# The players take turns playing, and in each turn, a player can select a tower with a height x and make a move. The move involves reducing the tower's height to a value y, where y is a divisor of x and satisfies the condition 1 < y < x. This means that a player can either decrease the tower's height by 1 or remove the entire tower, depending on the available options.
# 
# The game continues until one of the players is unable to make a move, signaling the end of the game. At this point, the player who cannot make a move is declared the loser, and the other player emerges as the winner.
# 
# Your task is to determine which player will emerge as the victor given the initial values of n and m. If Player 1 is the winner, you should return 1; otherwise, return 2.
# 
# If there is only one tower (n = 1), the game ends immediately, and Player 1 wins regardless of the tower's height (m =1).
# 
# If there is more than one tower (n > 1), If the height of each tower is 1 (m = 1), the game ends immediately, and Player 1 wins.
# If the height of any tower is even (m % 2 === 0), Player 2 wins regardless of the heights of the other towers.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Exercise-1
# input:
# 3 1
# output:
# 1
# 
# Exercise-2
# input:
# 4 2
# output:
# 2

# Solution:-

# Import Necessary Libraries
import sys

def towerBreakers(n, m):
    # If there is only one tower, Player 1 wins
    if n == 1:
        return 1
    # If the height of each tower is 1, Player 1 wins
    elif m == 1:
        return 1
    # If the height of any tower is even, Player 2 wins
    elif m % 2 == 0:
        return 2
    # Otherwise, Player 1 wins
    else:
        return 1


# Take Input
inputVal1, inputVal2 = map(int, input().split())

# Process Output Using Function
outputVal = towerBreakers(inputVal1, inputVal2)

# Print Output
print(outputVal)
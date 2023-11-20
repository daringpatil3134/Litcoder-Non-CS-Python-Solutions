# Restore IP Addresses
# The task at hand is to take a string of digits, denoted as 's', and add dots in appropriate positions to form valid IP addresses. A valid IP address consists of four distinct integers separated by a single dot.
# Each integer in the IP address must be within the range of 0 to 255, inclusive. Additionally, the integers should not have leading zeros. For example, "01" or "012" are not valid as they start with a zero.
# 
# To illustrate this, let's consider some examples.
# The string "25525511135" can be transformed into the IP address "255.255.111.35" because each integer falls within the valid range.
# 
# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.
# 
# Example
# 
# INPUT
# 0000
# 
# OUTPUT
# 0.0.0.0
# 
# Exercise-1
# 
# Input :
# 1001001010
# 
# Output :
# 100.100.10.10 100.100.101.0
# 
# Note: need to give one space between two IP addresses.
# 
# Exercise-2
# 
# Input:
# 192128172255
# 
# Output:
# 192.128.172.255

# Solution:-

#Import Necessary Libraries
import sys

def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append(".".join(path))
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]

            # Check for valid segment (no leading zeros and within the range 0-255)
            if (segment[0] == '0' and len(segment) == 1) or (segment[0] != '0' and 0 <= int(segment) <= 255):
                backtrack(end, path + [segment])

    result = []
    backtrack(0, [])

    # Convert the array to a string with spaces
    result_str = ' '.join(map(str, result))

    return result_str

#Take Input
inputVal = input()

#Process Output Using Function
outputVal = restore_ip_addresses(inputVal)

#Print Output
print(outputVal)
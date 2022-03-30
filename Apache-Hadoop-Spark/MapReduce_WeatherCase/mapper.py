#! /usr/bin/env python3

## MAPPER

# Import modules sys
import sys

# Create a new function which performs the following specific task to the given argument:
def myfunc(num):
    # Try the following piece of code:
    try:
        # Convert the given argument to 'integer'
        int(num)
        # Return the converted argument 
        return int(num)
    # If an error occurs in the previous step, handle this error by:
    except:
        # There is no code to execute here
        pass

# Get input from the terminal and for every 'line'/row:  
for line in sys.stdin:

## 'CLEANING' TEXT BY REMOVING SOME OBJECTS IN THE LINES/ROWS
    # Replace commas with blank
    words = line.replace(',', ' ')
    # Replace dashes with blank
    words = words.replace('-',' ')
    # Remove leading and trailing spaces from string 'line' and split it into a list
    words = words.strip().split()
    # Remove elements within list which lenght is four
    words = [word for word in words if len(word) != 4]
    # Apply function 'myfunc' to elements within the list
    words = [myfunc(word) for word in words]
    # Keep list elements as long as they are different than None
    words = [word for word in words if word != None]
    # If lenght of list is shorter than 4:
    if len(words)<4:
        # Skip the rest of code for this list and continue to next list/row
        continue
    # Assign the values in the second position within the list to variable 'key1'
    key1 = words[1]

##DEALING WITH OUTLIERS IN TEMPERATURE MEASURES. SETTING UPPER LIMIT TO 90 DEGREES
    # If values in the third position within the list are equal or lower than 90
    if words[2] <= 90:
        # Assign those values to to variable 'value1'
        value1 = words[2]
    # Print variables 'key1' and 'value1'
    print(key1,value1)


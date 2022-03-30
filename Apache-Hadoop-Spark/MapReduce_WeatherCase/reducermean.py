#! /usr/bin/env python

# REDUCER TO CALCULATE MEAN

# Import module sys
import sys


# Initialize variable 'date_sum' to None/Null and variable 'temp_sum' to 0
(date_sum, temp_sum) = (None, 0)
# Initialize variable 'date_count' to None/Null and variable 'temp_count' to 0
(date_count, temp_count) = (None,0)

# Get input from the terminal and for every 'line'/row:
for line in sys.stdin:
    # Split the string 'line' using ' ' as separator and assign resulted strings to variables 'date' and 'temp'
    (date,temp) = line.split(' ')
    # Convert string 'temp' to an integer
    temp = int(temp)

##ADDING THE TEMPERATURES
    # If 'date_sum' is already defined and 'date_sum' is not equal to given 'date':
    if date_sum and date != date_sum:
        # Print the current 'date_sum' and the division of 'temp_sum' by 'temp_count' as 'Daily mean'
        print "%s\t%s" % (date_sum, "Daily Mean: " + str(temp_sum/temp_count))
        # Assing given 'date' and 'temp' to 'date_sum' and 'temp_sum' respectively
        (date_sum, temp_sum) = (date, temp)
        
    # Otherwise:
    else:
        # Assign given 'date' to 'date_sum' and the sum of 'temp_sum' and 'temp' to 'temp_sum'
        (date_sum, temp_sum) = (date, temp_sum + temp)


#COUNTING THE TEMPERATURES
    # If 'date_count' is already defined and 'date_count' is not equal to given 'date':
    if date_count and date != date_count:
        # Assing given 'date' and '1' to 'date_count' and 'temp_count' respectively
        (date_count, temp_count) = (date, 1)
    # Otherwise:
    else:
        # Assign given 'date' to 'date_count' and 'temp_count' plus one to 'temp_count'
        (date_count, temp_count) = (date, temp_count + 1)    


# Print the last 'date_sum' and the division of 'temp_sum' by 'temp_count' as 'Daily mean'
print "%s\t%s" % (date_sum, "Daily Mean: " + str(temp_sum/temp_count))








    

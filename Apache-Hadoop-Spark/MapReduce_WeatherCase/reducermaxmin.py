#! /usr/bin/env python

## REDUCER TO FIND MINIMUM AND MAXIMUM

# Import module sys
import sys

# Initilize variable 'date_max' to None/Null and variable 'max_temp' to 0
(date_max, max_temp) = (None, 0)

# Iinitialize variable 'date_min' to None/Null and variable 'min_temp' to 0
(date_min, min_temp) = (None, 0)


# Get input from the terminal and for every 'line'/row:
for line in sys.stdin:
    # Split the string 'line' using ' ' as separator and assign resulted strings to variables 'date' and 'temp'
    (date,temp) = line.split(' ')
    # Convert string 'temp' to an integer
    temp = int(temp)

##FINDING MAX TEMP
    # If 'date_max' is already defined and 'date_max' is not equal to given 'date':
    if date_max and date_max != date:
        # Print the current 'date_max' and 'max_temp'
        print "%s\t%s" % (date_max, "Max Temp: " + str(max_temp))
        # Assing given 'date' and 'temp' to 'date_max' and 'max_temp' respectively
        (date_max, max_temp) = (date, temp)

    # Otherwise: 
    else:
        # Assign given 'date' to 'date_max' and the greater of 'max_temp' or 'temp' to 'max_temp'
        (date_max, max_temp) = (date, max(max_temp, temp))

## FINDING MIN TEMPERATURE
    # If 'date_min' is already defined and 'date_min' is not equal to given 'date':
    if date_min and date_min != date:
        # Print the current 'date_min' and 'min_temp'
        print "%s\t%s" % (date_min, "Min Temp: " + str(min_temp))
        # Assing given 'date' and 'temp' to 'date_min' and 'min_temp' respectively
        (date_min, min_temp) = (date, temp)

    # Otherwise:
    else:
        # Assign given 'date' to 'date_min' and the lowest of 'min_temp' or 'temp' to 'min_temp'
        (date_min, min_temp) = (date, min(min_temp, temp))

    
#Print the last 'date_max' and 'max_temp'
print "%s\t%s" % (date_max, "Max Temp: " + str(max_temp))
#Print the last 'date_min' and 'min_temp'
print "%s\t%s" % (date_min, "Min Temp: " + str(min_temp))

   

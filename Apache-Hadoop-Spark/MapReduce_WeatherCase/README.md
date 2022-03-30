## CALCULATING BASIC STATISTICS WITH MAPREDUCE ##
In this exercise I will solve a specific problem using the MapReduce
computational model. For this purpose, I'll use a sample dataset ("weather_measures.txt") to findsome descriptive statistics for temperature of each day of a given month for the year 2007.

Using the hourly data across all weather stations, I'll find:
* the daily maximum and minimum “Dry Bulb Temp” across all the weather stations
* the daily mean “Dry Bulb Temp” over all the weather stations
* the daily variance of “Dry Bulb Temp” over all the weather stations

Bear in mind that for this exercise I have only used the MapReduce framework and 
not any package to calculate the statistics.

"""
co2_ppm
Dylan Rhymaun
Print the standard deviation, mean, and
most recent recording of a list of
atmospheric pressures over time. 
"""

import csv
import math

lst = []

def mean(lst):  
    return sum(lst) / len(lst)

def std_dev(lst):
    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)  
    return math.sqrt(variance)
   

if __name__ == '__main__':
    # Read data from file into a list of floats
    with open('co2_ppm.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lst.append(float(row[1]))
            
    # Function calls for mean and standard deviation
    mean_value = mean(lst)  
    standard_deviation = std_dev(lst)
    most_recent = lst[-1]
    
    # Write results to file
    with open('results.txt', 'w') as results:
        results.write(f"Mean: {mean_value:.2f}\n")
        results.write(f"Standard Deviation: {standard_deviation:.2f}\n")
        results.write(f"Most recent observation: {most_recent:.2f}\n")

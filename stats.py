"""
'Stats'
Dylan Rhymaun
A program to help calculate both the mean
and standard deviation of a list of numbers
"""
import math

lst = []  

def calc_mean(lst):
    return sum(lst) / len(lst)

def std_dev(lst):
    mean = calc_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)  
    return math.sqrt(variance)  

if __name__ == '__main__':
    
    for _ in range(5):  
        number = float(input("Enter a real number: "))
        lst.append(number)
    
    mean_value = calc_mean(lst)  
    standard_deviation = std_dev(lst) 
    
    print(f"The mean is {mean_value:.3f} and the standard deviation is {standard_deviation:.3f}")

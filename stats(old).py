"""
'Stats'
Dylan Rhymaun
A program to help calculate both the mean
and standard deviation of a list jof numbers
"""
import math

lst = []

def calc_mean(lst):
    mean_value = sum(lst) / len(lst)

def std_dev(lst):
    mean = calc_mean(lst)
    sqrt(((number - calc_mean(lst)) ** 2 ) / len(lst))


if __name__ == '__main__':
    
    num1 = float(input("Enter a real number: "))
    num2 = float(input("Enter a real number: "))
    num3 = float(input("Enter a real number: "))
    num4 = float(input("Enter a real number: "))
    num5 = float(input("Enter a real number: "))
    
    for number in lst:
        lst.append(number)
        standard_deviation = std_dev(lst)
        
    print(f"The mean is {mean_value(lst):.3f} and the standard deviation is {standard_deviation:.3f}")
    
    
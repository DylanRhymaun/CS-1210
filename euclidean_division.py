"""
Euclidean Division
Dylan Rhymaun
A program that calculates a quotient
and remainder using euclidean division
"""

def calc_quotient(r, s):
    quotient = 0
    while r >= s:
        r -= s
        quotient += 1
    return quotient

def calc_remainder(r, s):
    while r >= s:
        r -= s
    return r

if __name__ == '__main__':
    
    r = int(input("Enter the dividend (a positive integer): "))
    s = int(input("Enter the divisor (a positive integer): "))
    
    quotient = calc_quotient(r, s)
    remainder = calc_remainder(r, s)
    
    print(f"{r} // {s} = {quotient}")
    print(f"{r} % {s} = {remainder}")

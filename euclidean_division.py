"""
Euclidean Division
Dylan Rhymaun
A program that calculates a quotient
and remainder using euclidean division
"""

def quotient(r, s):
    q = 0
    while r >= s:
        r -= s
        q += 1
    return q

def remainder(r, s):
    while r >= s:
        r -= s
    return r

if __name__ == '__main__':
    
    r = int(input("Enter the dividend (a positive integer): "))
    while r < 0:
        r = int(input("Enter the dividend (a positive integer): "))
    
    s = int(input("Enter the divisor (a positive integer): "))
    while s < 0:
        s = int(input("Enter the divisor (a positive integer): "))
    
    q = quotient(r, s)
    rem = remainder(r, s)
    
    print(f"{r} // {s} = {q}")
    print(f"{r} % {s} = {rem}")

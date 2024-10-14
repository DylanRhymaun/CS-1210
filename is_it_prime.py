"""
Is it prime?
Dylan Rhymaun
A program to check if...
"""

def prime_test(n):        
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
        

if __name__ == '__main__':
    n = int(input("Enter an integer > 1: "))
    while n >= 2:
        response = prime_test(n)
        if response == True:
            print(f'{n} is prime.')
        else:
            print(f'{n} is not prime.')
        break
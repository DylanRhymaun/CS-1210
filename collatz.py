"""
Collatz
Dylan Rhymaun
A program to generate a collatz sequence
"""

lst = []

def next_collatz(n):
    if n % 2 == 1:
        n = 3 * n + 1
            
    else:
        n = n // 2
    return n

if __name__ == '__main__':

    n = int(input("Enter an integer greater than 1: "))
    lst.append(n)
    
    while n != 1:
        n = next_collatz(n)
        lst.append(n)
    
    print(f'{lst}')
    print(f'The length of the sequence is {len(lst)}')
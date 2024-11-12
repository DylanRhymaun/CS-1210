"""

Dylan Rhymaun

"""
import os

if __name__ == '__main__':
    
    with open('winter.txt', 'r') as fh:
        for line in fh:
            print(line, end='')  

print("Current Working Directory:", os.getcwd())
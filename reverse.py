"""
Reverse
Dylan Rhymaun
Reverses the order of characters in a provided string
"""

stack = []

if __name__ == '__main__':
    
    word = (input("Enter a string, and I'll print it backwards! "))
    for letter in word:
        stack.append(letter)
        
    while stack:
        print(stack.pop(), end='')
    print()    
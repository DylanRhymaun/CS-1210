"""
Balanced
Dylan Rhymaun
Checks if an input contains balanced parenthesis
"""

stack = []
def balanced(s):
    for p in s:
        if p == "(":  
            stack.append(p)
        elif p == ")":  
            if not stack:  
                return False
            stack.pop()  
    
    return len(stack) == 0  

if __name__ == '__main__':
    s = input("Enter a string containing parentheses: ")
    if balanced(s) == True:
        print("Parentheses are balanced!")
    else:
        print ("Parentheses are not balanced!")
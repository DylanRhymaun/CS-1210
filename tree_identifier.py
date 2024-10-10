"""
Tree identifier
Dylan Rhymaun
Determines tree species based on characteristics
"""

response = (input('Leaves (l) or needles (n)? l/n '))
if response.lower() == 'l':
    response = (input('Simple (s) or compound (c)? s/c '))
    if response.lower() == 's':
        print('Maple')
    elif response.lower() == 'c':
        print('Ash')
    else:
        print('Invalid choice for simple or compound! Restart program.')

elif response.lower() == 'n':
    response = (input('Individual (i) or clustered (c)? i/c '))
    if response.lower() == 'i':
        print('Spruce')
    elif response.lower() == 'c':
        print('Pine')
    else:
        print('invalid choice for individual or clustered! Restart program.')
        
else:
    print('invalid choice for leaves or needles! Restart program.')
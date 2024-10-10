"""
Temperature Unit Conversion Tabel
Dylan Rhymaun
Enter a degree in Fareinheit and convert it to Celsius
"""

def f_to_c(F):
    C=(F - 32)/1.8
    return C

F = float(input('Enter temperature in Degrees F: '))
C_minus = f_to_c(F - 10)
C = f_to_c(F)
C_plus = f_to_c(F + 10)

print(f'{"Fareinheit":<12}'
      f'{"Celsius":<12}')
#F-10
print(f'{F - 10:<12.1f}'
      f'{C_minus:<12.1f}')
#F+0
print(f'{F + 0:<12.1f}'
      f'{C:<12.1f}')
#f+10
print(f'{F + 10:<12.1f}'
      f'{C_plus:<12.1f}')
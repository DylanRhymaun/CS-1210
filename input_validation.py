"""
Dylan Rhymaun

This program calculates the gravitational force between two masses.
It uses input validation to ensure positive, numeric values are entered.
"""

G = 6.67430 * 10 ** -11

def calc_force(m1, m2, r):
    return G * (m1 * m2) / r ** 2


if __name__ == '__main__':
    while True:
        try:
            m_01 = float(input("Enter the mass of body 1 in kg: "))
            if m_01 > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for body 1.")
    
    while True:
        try:
            m_02 = float(input("Enter the mass of body 2 in kg: "))
            if m_02 > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for body 2.")
    
    while True:
        try:
            d = float(input("Enter the distance between the centers of "
                            "the bodies in meters: "))
            if d > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the "
                  "distance.")

    f = calc_force(m_01, m_02, d)
    print(f"The gravitational force is {f:,.4f} Newtons")
"""
Element and Atomic Number Converter
Dylan Rhymaun
Converts atomic numbers to their element, and vice versa
"""

ELEMENTS = (None, "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
            "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium",
            "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur",
            "Chlorine", "Argon", "Potassium", "Calcium", "Scandium",
            "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt",
            "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
            "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
            "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
            "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium",
            "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium",
            "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
            "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
            "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
            "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium",
            "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
            "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
            "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
            "Plutonium", "Americium", "Curium", "Berkelium", "Californium",
            "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
            "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium",
            "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
            "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine",
            "Oganesson")

if __name__ == '__main__':

    method = input("Lookup by element name (e) or atomic number (n)? (e/n) ")

    if method.lower() == 'e':
        element_name = input('what is the name of your element? ').capitalize()
        if element_name in ELEMENTS:
            element_index = ELEMENTS.index(element_name)
            print(f'The atomic number of {element_name} is {element_index}')
        else:
            print("error - invalid. Restart and enter the name of an element")

    elif method.lower() == 'n':
        element_number = int(input(
            'what is the atomic number of your element? '))
        if 0 < element_number <= len(ELEMENTS):
            element_name = ELEMENTS[element_number]
            print(
                f'The element with an atomic number of \
{element_number} is {element_name}')
        else:
            print("error - invalid. Restart and \
enter a number between 1 and 118")

    else:
        print("error - Invalid, please restart program")

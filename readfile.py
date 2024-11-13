"""
readfile
Dylan Rhymaun
Takes a file name and prints contents
if file is found.
"""
import os

if __name__ == '__main__':
    
    def read_file():
        while True:
            filename = input("Enter a filename (or 'q' to quit): ")
            if filename.lower() == 'q':
                print("Program terminated")
                break
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print(content)
                    break
            except FileNotFoundError:
                print(f"The file '{filename}' was not found.")

read_file()
"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""

def main():
    
    num1 = float(input("\033[1;3m Type a number to see its square: \033[0m"))
    square = num1 ** 2
    print(f"The Square of {num1} squared is {square}")

if __name__ == "__main__":
    main()
"""The provided solution demonstrates a working implementation of this problem, where the main()
function guides the user through the process of entering two numbers
and displays their sum."""


def main():
    print("This program add to numbers.")
    num1 = input("\033[1;3m Enter the first number: \033[0m")
    num1 = int(num1)

    num2 = input("\033[1;3m Enter the second number: \033[0m")
    num2 = int(num2)

    total = num1 + num2
    print(f"Sum of The Two numbers is {total}.")
    
    
if __name__ == "__main__":
    main()
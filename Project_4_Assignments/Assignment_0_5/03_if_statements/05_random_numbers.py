import random

diff_number:int = 10
min_value:int = 1
max_value:int = 100

def main():
    for i in range(diff_number):
        i = random.randint(min_value, max_value)
        print(i, end=" ")

if __name__ == "__main__":
    main()
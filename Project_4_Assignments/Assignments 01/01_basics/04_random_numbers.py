import random

def main():
    for i in range(10):
        print(random.randint(1, 100), end = " ")
        
if __name__ == "__main__":
    main()



N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE , MAX_VALUE), end = " ")
  

if __name__ == '__main__':
    main()
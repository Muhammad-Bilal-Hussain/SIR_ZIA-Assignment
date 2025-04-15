import random

def main():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    tries = 0

    while guess != secret_number:
        try:
            guess = int(input("Take a guess: "))
            tries += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {tries} tries.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

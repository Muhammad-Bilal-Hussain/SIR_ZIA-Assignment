def main():
    print("🧠 Think of a number between 1 and 100 and I’ll try to guess it!")
    print("When I guess, type: 'low', 'high', or 'correct'.")

    low = 1
    high = 100
    tries = 0

    while True:
        guess = (low + high) // 2
        tries += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it 'low', 'high', or 'correct'? ").lower()

        if feedback == "low":
            low = guess + 1
        elif feedback == "high":
            high = guess - 1
        elif feedback == "correct":
            print(f"🎉 Yay! I guessed your number in {tries} tries.")
            break
        else:
            print("Please type 'low', 'high', or 'correct' only.")

if __name__ == "__main__":
    main()

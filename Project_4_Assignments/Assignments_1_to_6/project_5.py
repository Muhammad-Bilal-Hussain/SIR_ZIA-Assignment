import random

def choose_word():
    words = ["python", "hangman", "coding", "program", "developer", "laptop"]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def main():
    secret_word = choose_word()
    guessed_letters = []
    tries = 6

    print("🎯 Welcome to the Hangman Game!")
    print("Guess the word before you run out of tries!\n")

    while tries > 0:
        print(f"Word: {display_word(secret_word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Tries Left: {tries}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good guess!\n")
        else:
            print("❌ Wrong guess.\n")
            tries -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 Congrats! You guessed the word: {secret_word}")
            break
    else:
        print(f"💀 Game Over! The word was: {secret_word}")

if __name__ == "__main__":
    main()

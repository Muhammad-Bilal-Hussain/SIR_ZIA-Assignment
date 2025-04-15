import random

def main():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("👊 Welcome to Rock, Paper, Scissors Game with Score!")
    print("Type 'quit' anytime to end the game.\n")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice == "quit":
            print("\n🏁 Game Over!")
            print(f"👤 Your Score: {user_score}")
            print(f"💻 Computer Score: {computer_score}")
            if user_score > computer_score:
                print("🏆 You Win the Game!")
            elif user_score < computer_score:
                print("😢 Computer Wins the Game!")
            else:
                print("😐 It's a Tie Overall!")
            break

        if user_choice not in options:
            print("❌ Invalid choice. Try again.\n")
            continue

        computer_choice = random.choice(options)
        print(f"💻 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    main()

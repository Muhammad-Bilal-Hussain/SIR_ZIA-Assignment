import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

def main():
    print("🎯 Welcome to the Countdown Timer!")
    try:
        total_time = int(input("Enter time in seconds: "))
        countdown(total_time)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()

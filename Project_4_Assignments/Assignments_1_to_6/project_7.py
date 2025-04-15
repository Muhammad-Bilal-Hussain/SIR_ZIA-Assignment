import random
import string

# Function to generate a password
def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    
    # Add different character sets based on user preferences
    if use_letters:
        characters += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_digits:
        characters += string.digits  # Includes digits from 0-9
    if use_symbols:
        characters += string.punctuation  # Includes punctuation symbols

    # If no character set is selected, set a default
    if not characters:
        characters = string.ascii_letters  # Default to letters if nothing is selected
    
    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Get user inputs
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    password = generate_password(length, use_letters, use_digits, use_symbols)

    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

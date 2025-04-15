def main():
    print("Welcome to the Mad Libs game!")

    # User inputs
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Story
    print("\nHere's your story:")
    print(f"One day, a {adjective} {noun} decided to {verb} at the {place}.")
    print("Everyone who saw it was amazed!")

if __name__ == "__main__":
    main()

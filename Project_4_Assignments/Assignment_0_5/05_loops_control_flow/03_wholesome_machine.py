affirmation:str = "I am capable of doing anything I put my mind to."


def main():
    
    print("Please type the following affirmation:", affirmation)
    
    user_feedback:str = input()
    while user_feedback != affirmation:
        print("That was not the affirmation. Please try again.")
        
        print("Please type the following affirmation: ", affirmation)
        
        user_feedback:str = input()
        
    print("That's right! :)")
    
    
if __name__ == "__main__":
    main()
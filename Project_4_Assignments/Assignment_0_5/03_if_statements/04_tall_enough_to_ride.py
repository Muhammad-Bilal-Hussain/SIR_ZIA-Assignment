def main():
    
    MINIMUM_HEIGHT:int = 50
    user_height = int(input("How tall are you? "))
    
    if MINIMUM_HEIGHT <= user_height:
       print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
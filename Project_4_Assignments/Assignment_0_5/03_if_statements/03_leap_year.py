def main():
    
    year:int = int(input("Enter a year: "))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("1 That's a leap year!")
            else:
                print("2 That's not a leap year.")
        else:
            print("3 That's a leap year!")    
    else:
        print("4 That's not a leap year.")

if __name__ == "__main__":
    main()
# The code checks if a given year is a leap year based on the rules of the Gregorian calendar.
Peturksbouipo:int = 16
Stanlau:int = 25
Mayengua:int = 48

def main():
    
    user_age:int = int(input("How old are you? "))
    
    if user_age >= Peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo}.")
        
    if user_age >= Stanlau:
        print(f"You can vote in Stanlau where the voting age is {Stanlau}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau}.")         
        
    if user_age >= Mayengua:
        print(f"You can vote in Mayengua where the voting age is {Mayengua}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua}.")
        
        
        
        
if __name__ == "__main__":
    main()
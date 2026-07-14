def showBalance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Enter a positive number")
    else:
        return amount

def withdraw(balance):
    
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("Insufficent funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount

def main():
    # GLOBAL VARIABLES
    balance = 0
    is_running = True

    while is_running:
        print()
        print("#####################")
        print("Banking Program")
        print("#####################")
        print()
        print("1) Show Balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Exit")
        print()
        choice = input("Enter a number (1-4): ")
        print()

        if choice == '1':
            showBalance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("Thank you have a wonderful day :)")
            print()
            is_running = False
        else:
            print("Please enter a valid choice.")
            print()

if __name__ == '__main__':
    main()
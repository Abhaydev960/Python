balance = 5000.0
pin = "1234"
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Available balance: Rs. {balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter deposit amount: Rs. "))
            if amount > 0:
                balance += amount
                print("Deposit successful.")
            else:
                print("Enter a positive amount.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: Rs. "))
            if 0 < amount <= balance:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Invalid amount or insufficient balance.")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Try again.")

balance = 0

print("🏦 Welcome to Mini Banking System")

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"💰 Your current balance is: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        else:
            print("❌ Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Invalid amount.")
        else:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")

    elif choice == "4":
        print("👋 Thank you for using the Mini Banking System!")
        break

    else:
        print("⚠️ Invalid choice. Please try again.")

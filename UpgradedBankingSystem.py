balance = 0
pin = "1234"
transactions = []

print("🏦 Welcome to Secure Mini Banking System")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("❌ Incorrect PIN. Access Denied.")
    exit()

print("✅ Login successful!")

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"💰 Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited ₹{amount}")
            print("✅ Deposit successful.")
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
            transactions.append(f"Withdrew ₹{amount}")
            print("✅ Withdrawal successful.")

    elif choice == "4":
        if len(transactions) == 0:
            print("📭 No transactions yet.")
        else:
            print("\n📜 Transaction History:")
            for t in transactions:
                print("-", t)

    elif choice == "5":
        print("👋 Logged out safely. Thank you!")
        break

    else:
        print("⚠️ Invalid choice. Try again.")

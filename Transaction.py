# Parent Class
class Transaction:
    def process(self):
        print("Processing transaction...")


# Child Class - Deposit
class Deposit(Transaction):

    # Method Overloading (using default parameter)
    def deposit(self, amount, bonus=0):
        total = amount + bonus
        print(f"Deposited: {total}")

    # Method Overriding
    def process(self):
        print("Deposit transaction processed.")


# Child Class - Withdrawal
class Withdrawal(Transaction):

    def withdraw(self, amount):
        print(f"Withdrawn: {amount}")

    # Method Overriding
    def process(self):
        print("Withdrawal transaction processed.")


# Child Class - Transfer
class Transfer(Transaction):

    def transfer(self, amount, receiver):
        print(f"Transferred {amount} to {receiver}")

    # Method Overriding
    def process(self):
        print("Transfer transaction processed.")


# Demonstration
print("=== Banking System ===")

# Deposit
d = Deposit()
d.deposit(50000)          # Overloading version 1
d.deposit(50000, 5000)   # Overloading version 2
d.process()

print()

# Withdrawal
w = Withdrawal()
w.withdraw(20000)
w.process()

print()

# Transfer
t = Transfer()
t.transfer(10000, "Gena")
t.process()
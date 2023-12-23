class bankaccount:
     def __init__(self,account_number,pin,balance=0):
         self.account_number=account_number
         self.pin=pin
         self.balance=balance

     def login(self,entered_pin):
         if entered_pin==self.pin:
             print ("Login successful!")
             return True
         else:
             ("Incorrect PIN,Login failed.")
             return False

     def deposit(self,amount):
         if amount>0:
             self.balance+=amount
             print(f"Amount{amount} deposited.Current balance{self.balance}")
         else:
             print("Invalid amount for deposite")

     def withdraw(self,amount):
         if amount>0:
             if amount<=self.balance:
                 self.balance-=amount
                 print(f"Amount {amount} withdraw. Current balance: {self.balance}")
             else:
                 print("Insufficient balance")

         else:
             print("Invalid amount for withdrawal.")

     def check_balance(self):
         print(f"Current balance:{self.balance}")


account1=bankaccount("12345678","1234",1000)
entered_pin=input("Enter PIN:")
if account1.login(entered_pin):
    while True:
        print("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
        choice=input("Enter your choice(1/2/3/4):")

        if choice=="1":
            amount_to_deposit=float(input("Enter amount to deposit:"))
            account1.deposit(amount_to_deposit)
        elif choice=="2":
            amount_to_withdraw=float(input("Enter amount to withdraw:"))
            account1.withdraw(amount_to_withdraw)
        elif choice == "3":
            account1.check_balance()
        elif choice == "4":
            print("Exiting.Thank you!")
            break
        else:
            print("Invalid choice.Please chose a valid option.")
class Bank:
    def __init__(self,bank_name,account_number,limit,total_account_count,balance):
        self.bank_name = bank_name
        self.account_number = account_number
        self.limit = limit
        self.total_account_count = total_account_count
        self.balance = balance
    def Account_number(self):
        return f"The account number is {self.account_number}"
    def Limit(self):
        return f"The limit is {self.limit}"
    def Change_Limit(self,change_limit):
        self.limit = change_limit
        return f"Your New Limit is {self.limit}"
    def Get_details(self):
            return f"The bank is {self.bank_name}\nThe account number is {self.account_number}\nThe limit is {self.limit}\nYou have {self.total_account_count} accounts\nYour Balance is {self.balance}"
    def get_Total_account(self):
        return f"You have {self.total_account_count} accounts"
    def Change_Bank(self,another_bank):
        self.bank_name = another_bank
        return f"The bank is changed to {self.bank_name}"
    def Check_balance(self):
        return f"Your Balnance is {self.balance}"
    def withdrwal_amount(self,withdrwal):
        if self.balance >= withdrwal:
            self.balance -= withdrwal
            print("Withdrwal accepted")
        else:
            print("Funds Unavilable")
    def deposite(self,de_po):
        self.balance += de_po
        print("Depoiste accepted")
    def tarnsfer(self,transfer_amount):
        self.balance += transfer_amount 
b1 = Bank("HBL",1908766,30000,4,12000)
print(b1.Get_details())







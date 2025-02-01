class Bank:
    bank_name = "SBI" # Class Variable
    def __init__(self,name,age,balance):
        self.user_name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        print(f"User name: {self.user_name} and User Balance: {self.balance} for Bank: {Bank.bank_name}")
b1 = Bank('Pooja',22,55000)
print(b1.bank_name)
print(Bank.bank_name)
b1.get_info()
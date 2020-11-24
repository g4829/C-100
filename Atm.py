class Atm(object):
    def __init__(self,atmCardNumber,pinNumber,cashWithdrawel,balance):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber
        self.cashWithdrawel=cashWithdrawel
        self.balance=balance
    
    def number(self):
        print("INSERT CARDNUMBER")

    def pin(self):
        print("INSERT PIN NUMBER")

    def cash(self):
        print("ENTER THE AMOUNT")

    def Balance(self):
        print("BALANCE LEFT")

ICICI=Atm(230444242,4698,1000,1000)
YESBANK=Atm(230344242,4898,2000,1500)

print(ICICI.number())
print(ICICI.pin())
print(ICICI.cash())
print(ICICI.Balance())
print(YESBANK.number())
print(YESBANK.pin())
print(YESBANK.cash())
print(YESBANK.Balance())
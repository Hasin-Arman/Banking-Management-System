from datetime import date
import time
class person:
    def __init__(self,name,address,profession):
        self.name = name
        self.address = address
        self.profession = profession
class Bank:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.user_info={}
class User(person):
    flag=100
    def __init__(self,name,address,profession):
        super().__init__(name,address,profession)
        self.user_id =None
        self._email=None
        self.__password=None
        self.transaction_start=None
        self.transaction_date=None
        self.bank_balance=0
        self.loan_taken=0

    def create_account(self,email,password):
        self._email=email
        self.__password=password
        self.user_id =User.flag
        User.flag+=1

    def deposit_money(self,amount,bank):
        if amount > 0:
            self.bank_balance+=amount
            bank.money+=amount
            print('Money deposited successfully')
    
    def withdraw_money(self,amount,bank):
            if amount <=self.bank_balance:
                if(amount < bank.money):
                    self.bank_balance-=amount
                    bank.money-=amount
                    print('Money withdrwan successfully')
                else:
                    print('The bank is bankrupted')
            else:
                print('Don\'t have enough money to withdraw')
    
    def check_balance(self):
        print(self.bank_balance)
    
    def transfer_balance(self,bank,receiver,amount):
        if self.bank_balance > 0:
            if receiver in bank.user_info:
                current_time = time.strftime("%H:%M:%S")
                self.transaction_start=current_time
                self.transaction_date=date.today()
                bank.user_info[receiver]['Balance']+=amount
                self.bank_balance-=amount
            else:
                print('Receiver not found')
        else:
            print('Not enough money to transfer')

    def check_transfer_history(self,bank,receiver):
        print('Sender Name: ',self.name)
        print('Transaction Time : ',self.transaction_start)
        print('Transaction Time : ',self.transaction_date)
        print('Receiver Name: ',bank.user_info[receiver]["Name"])
        print('Money send: ',(bank.user_info[self.user_id]["Balance"]-bank.user_info[receiver]["Balance"]))
    
    def take_loan(self,amount,admin):
        if(admin.loan_feature=='on'):
            if amount<=self.bank_balance*2:
                self.loan_taken+=amount
                self.bank_balance+=amount
        else:
            print('Sorry,loan can not be provided right now')

    
class Admin(person):
    def __init__(self,name,address,profession):
        super().__init__(name,address,profession)
        self._email = None
        self.__password = None
        self.loan_feature=None
        
    def add_user(self,user,bank):
        bank.user_info[user.user_id]={'Name':user.name,'Address':user.address,'profession':user.profession,'Balance':user.bank_balance,'Loan Taken':user.loan_taken}

    def create_account(self,email,password):
        self._email=email
        self.__password=password
    
    def check_available_balance(self,bank):
        print(bank.money)

    def total_loan_taken(self,bank):
        self.id=100
        total_loan=0
        for user in bank.user_info:
            total_loan+=bank.user_info[self.id]['Loan Taken']
            self.id+=1
        print('Total Loan: ', total_loan)

    def loan(self,feature):
        if(feature=='on'):
            self.loan_feature='on'
        else:
            self.loan_feature='off'

chayan=User('chayan', 'ctg', 'student')
chayan.create_account('hasin@gmail.com', 123)
admin=Admin('hakuna', 'dhaka', 'useless')
bank=Bank('phitron',50000)
chayan.deposit_money(10000,bank)
chayan.withdraw_money(3000, bank)
admin.loan('on')
chayan.take_loan(5000,admin)
chanchal=User('chanchal', 'bogura', 'job')
chanchal.create_account('chanchal@gmail.com', 123)
admin.add_user(chayan,bank)
admin.add_user(chanchal,bank)
chayan.transfer_balance(bank, 101, 5000)
chayan.check_transfer_history(bank, 101)
admin.total_loan_taken(bank)
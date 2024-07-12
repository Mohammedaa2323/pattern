class Bank :
    ac_num:int
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:int
    # amount:int

    def set_acc(self,ac_num,name,ac_type,ifsc_code,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.ac_num} has been creaditd with {amount} aval bal is {self.balance}")

    
    def display_acc(self):
        print(self.ac_num,self.name,self.ac_type,self.ifsc_code,self.branch,self.balance)

    def withdraw(self,amount):

        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.ac_num} has been debited with {amount} aval bal is {self.balance}")

    def get_balance(self):
        print("your aval bal is",self.balance)

acc=Bank()
acc.set_acc(987654321,"mohammed","savings","CNRIFC","perumbilavu",20000)
acc.display_acc()
acc.deposit(5000)
acc.withdraw(1000)
acc.get_balance()
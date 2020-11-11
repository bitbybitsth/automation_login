from abc import ABC, abstractmethod

from sample import SavingsAccount


class RBI(ABC):

    @abstractmethod
    def provide_savings_account(self):
        pass

    @abstractmethod
    def provide_passbook(self):
        pass

    @abstractmethod
    def amount_withdrawal(self):
        pass

    @abstractmethod
    def amount_deposit(self):
        pass


class BankOfBaroda(RBI):
    all_accounts = []

    def amount_deposit(self, acc_holder, amount, contact):
        account = self.get_account(acc_holder)
        if account:
            account.acc_balance += amount
            return f"Amount deposited"
        else:
            print("Creating your account")
            s2 = SavingsAccount(2, acc_holder, amount, contact)
            return f"Your account has been created, account_no is {s2.acc_no}"

    def provide_passbook(self):
        pass

    def provide_savings_account(self):
        s1 = SavingsAccount(1, "pankaj", 50000, 9766588937)
        self.all_accounts.append(s1)

    def get_account(self, acc_holder):
        for item in self.all_accounts:
            if item.acc_holder == acc_holder:
                return item

    def amount_withdrawal(self, acc_holder, withdrawal_amount):
        account = self.get_account(acc_holder)
        if account:
            min_balance = account.acc_balance - withdrawal_amount
            if min_balance > 1000:
                account.acc_balance -= withdrawal_amount
                return f"{withdrawal_amount} has been withdrawal from your account"
            else:
                return "you have to maintain minimum balance"
        else:
            return f"You don't have a account in our bank"

    def online_banking(self):
        pass

    def no_transaction_fee(self):
        pass


all_accounts = []

class ICICI(RBI):

    all_accounts = []

    def amount_deposit(self, acc_holder, amount, contact):
        account = self.get_account(acc_holder)
        if account:
            account.acc_balance += amount
            return f"Amount deposited"
        else:
            print("Creating your account")
            s2 = SavingsAccount(2, acc_holder, amount, contact)
            return f"Your account has been created, account_no is {s2.acc_no}"

    def provide_passbook(self):
        pass

    def provide_savings_account(self):
        s1 = SavingsAccount(1,"pankaj", 50000, 9766588937)
        self.all_accounts.append(s1)

    def get_account(self, acc_holder):
        for item in self.all_accounts:
            if item.acc_holder == acc_holder:
                return item

    def amount_withdrawal(self, acc_holder, withdrawal_amount ):
        account = self.get_account(acc_holder)
        if account:
            min_balance = account.acc_balance - withdrawal_amount
            if min_balance>1000:
                account.acc_balance -= withdrawal_amount
                return f"{withdrawal_amount} has been withdrawal from your account"
            else:
                return "you have to maintain minimum balance"
        else:
            return f"You don't have a account in our bank"


    def online_banking(self):
        pass

    def no_transaction_fee(self):
        pass


class HDFC(RBI):

    all_accounts = []
    def amount_deposit(self, acc_no, amount):
        account = self.get_account(acc_no)
        if account:
            account.acc_balance += amount
            return f"Amount deposited"
        else:
            inp = input("You don't have a account Here, Press y to create or n to quit")
            if inp == 'y':
                s2 = SavingsAccount(acc_no, acc_balance=amount, acc_holder="honu", contact_no=467653476)
                return f"Your account has been created, account_no is {s2.acc_no}"
            else:
                return "Thank you for visiting us"


    def provide_passbook(self):
        pass

    def provide_savings_account(self):
        s2 = SavingsAccount(1, "pankaj", 50000, 9766588937)
        s2.IFSC = "HDFC0003627"
        self.all_accounts.insert(0,s2)

    def get_account(self, acc_nnumber):
        for item in self.all_accounts:
            if item.acc_no == acc_nnumber:
                return item

    def amount_withdrawal(self, acc_no, withdrawal_anount):
        account = self.get_account(acc_no)
        if account:
            if account.acc_balance >=withdrawal_anount:
                account.acc_balance -= withdrawal_anount
                return f"{withdrawal_anount} has been withdrawal from your account"
            else:
                return "no sufficient funds"
        else:
            return "You are not a member of our bank"





ic = ICICI()
hd = HDFC()
ic.provide_savings_account()
hd.provide_savings_account()
result = hd.amount_deposit(5,4000)




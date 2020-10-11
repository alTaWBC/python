import datetime
import pytz
from typing import List


class Account:
    """Simple account class with balance
    """

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    @staticmethod
    def _format_date(date):
        return date.strftime("%a, %d-%m-%y %H:%M:%S")

    def __init__(self, name, balance):
        self._name = name  # Tells variable is not supposed to be changed
        # Hides variable (To consult we need to use _Account__balance)
        self.__balance = balance
        self._transactions: List[(datetime.datetime, int)] = [
            (Account._current_time(), balance)]
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transactions.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transactions.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and \
no more than you balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        date, amount = self._transactions[0]
        print(f"{amount:6} was used to open account on {Account._format_date(date)} \
(local time was {Account._format_date(date.astimezone())})")
        for date, amount in self._transactions[1:]:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} was {tran_type} on {Account._format_date(date)} \
(local time was {Account._format_date(date.astimezone())})")


if __name__ == '__main__':
    account = Account("Lua", 50000000000)
    account.withdraw(10)
    account.deposit(100)
    account.withdraw(1000000000000000000)
    account.deposit(-10)
    account.show_transactions()

    # Variable exists but his hidden and will show error
    account._Account__balance = 40

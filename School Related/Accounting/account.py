# account class
# Add Ability to add account alias
# add docstrings

# is it nessesary to have journalTrans and Account Trans as two different objects?
# probably not, but can merge later after implimentation
#(aka never)
# maybe make journal own class?


class JournalTranscation(object):
    """docstring for JournalTranscation"""

    def __init__(self, transactionID, debitOrCredit, amount, account):
        self.transID = transactionID
        self.debitOrCredit = debitOrCredit
        self.amount = amount
        self.account = account


class Journal(object):
    """docstring for Journal"""

    def __init__(self):
        self.journalTrans = []

    def AddTransaction(self, transactionID, debitOrCredit, amount, account):
        self.journalTrans.append(JournalTranscation(
            transactionID, debitOrCredit, amount, account))

    def RemoveTransaction(self, transactionID):
        for x in self.journalTrans:
            if x.transID == transactionID:
                self.journalTrans.remove(x)

    def TestAccountingEquation(self):
        pass

    def HypoChangeToAccounts():
        pass

# TODO
# Fix Output
    def PrintJournal(self):
        print('=' * 20)
        for x in self.journalTrans:
            output = ''
            output += str(x.transID).ljust(2)
            if x.debitOrCredit == "cr":
                output += "   "
            output += str(x.debitOrCredit).ljust(3)
            output += str(x.account).ljust(15)
            output += str(x.amount)
            print(output)
        print("=" * 20)


class AccountTransaction(object):
    """docstring for AccountTransaction"""

    def __init__(self, debitOrCredit, amount, transactionID):
        self.transID = transactionID
        self.debitOrCredit = debitOrCredit
        self.amount = amount


class Account(object):
    """docstring for ClassName"""

    def __init__(self, accountName, debitOrCredit):
        self.accountName = accountName
        self.debitOrCredit = debitOrCredit
        self.transationList = []

    def AddTransaction(self, debitOrCredit, amount, transactionID):
        if debitOrCredit == "dr":
            debitOrCredit = "debit"
        elif debitOrCredit == "cr":
            debitOrCredit = "credit"

        self.transationList.append(AccountTransaction(
            debitOrCredit, amount, transactionID))
    # TODO it is just an inverse, probably can make better

    def CalculateBalance(self):
        accountBalance = 0
        if self.debitOrCredit == "debit":
            for x in self.transationList:
                if x.debitOrCredit == "debit":
                    accountBalance += x.amount
                elif x.debitOrCredit == "credit":
                    accountBalance -= x.amount
        elif self.debitOrCredit == "credit":
            for x in self.transationList:
                if x.debitOrCredit == "credit":
                    accountBalance += x.amount
                elif x.debitOrCredit == "debit":
                    accountBalance -= x.amount
        return accountBalance

    def PrintAccount(self):

        debitTrans = []
        creditTrans = []
        for x in self.transationList:
            if x.debitOrCredit == "debit":
                debitTrans.append((x.transID, x.amount))
            elif x.debitOrCredit == "credit":
                creditTrans.append((x.transID, x.amount))

        print("     " + self.accountName + " Account")
        print("Debit Transactions")
        for ID, amount in debitTrans:
            print("  " + str(ID) + "     " + str(amount))
        print("Credit Transactions")
        for ID, amount in creditTrans:
            print("  " + str(ID) + "     " + str(amount))
        print("-" * 20)

        print("Account Total:")
        print(self.CalculateBalance())


if __name__ == '__main__':
    cashAccount = Account("Accounts Payable", "credit")
    cashAccount.AddTransaction("debit", 500, 1)
    cashAccount.PrintAccount()

import account

# TODO
# CLI Add Account
# Add Journal
# Add Basic account equation check in add account
# Add unit testing
# export csv


def ParseInput(userInput):
    return userInput.split(" ")

# Add support for alias in IsThisAnAccount


def IsThisAnAccount(name):
    for acc in accountsList:
        if name == acc.accountName:
            return True
    return False


def checkNone(*args):
    if any(arg is None for arg in args):
        return False
    return True

# This Hurts me


def AccountTransaction(userInput, transNumber):
    userInputIndex = 0
    for x in userInput:
        workingAccountName = None
        workingTransAmount = None
        workingTransType = None
        if x == 'dr' or x == 'cr':
            workingTransType = x

            if IsThisAnAccount(userInput[userInputIndex + 1]):
                workingAccountName = userInput[userInputIndex + 1]
            if userInput[userInputIndex + 2].isdigit():
                workingTransAmount = int(userInput[userInputIndex + 2])

            # Adding Transaction to the Journal and Account
            # Add some accounting equation check here
            if checkNone(workingAccountName, workingTransAmount, workingTransType):
                # Add trans to journal
                tJournal.AddTransaction(transNumber, workingTransType, workingTransAmount, workingAccountName)
                # Add trans to Accounts
                for acc in accountsList:
                    if acc.accountName == workingAccountName:
                        acc.AddTransaction(
                            workingTransType, workingTransAmount, transNumber)
            else:
                print(workingAccountName, workingTransAmount, workingTransType)
                print("Error invalid Arguments")
        userInputIndex += 1


def AddDefaultAccounts():
    accountsList.append(account.Account("cash", "debit"))
    accountsList.append(account.Account("supplies", "debit"))
    # Expense
    accountsList.append(account.Account("wagesExp", "credit"))
    accountsList.append(account.Account("rentExp", "credit"))
    accountsList.append(account.Account("utilitesExp", "credit"))
    # Revanue
    accountsList.append(account.Account("rentRev", "debit"))
    accountsList.append(account.Account("serviceRev", "debit"))
    # SE
    accountsList.append(account.Account("commonStock", "credit"))
    accountsList.append(account.Account("RE", "credit"))


def PrintAccount(userInput):
    print("=" * 20)
    for x in accountsList:
        if userInput[1] == x.accountName:
            x.PrintAccount()
    print("=" * 20)


def PrintAccountList():
    print("Number of Accounts:" + str(len(accountsList)))
    print("=" * 20)
    for x in accountsList:
        print("{}, {}".format(x.accountName, x.debitOrCredit))
    print("=" * 20)


def PrintUnajustedTrialBal():
    print("=" * 20)
    # TODO
    # Clean Up
    credits = 0
    debits = 0
    for x in accountsList:
        output = ''
        if x.debitOrCredit == "debit":
            output += str(x.accountName[0:15])
            output = output.ljust(20)
            output += str(x.CalculateBalance())
            print(output)
            debits += x.CalculateBalance()
    for x in accountsList:
        output = ''
        if x.debitOrCredit == "credit":
            output += str(x.accountName[0:10])
            output = output.ljust(25)
            output += str(x.CalculateBalance())
            print(output)
            credits += x.CalculateBalance()
    print("-" * 20)
    trialBalance = 'Final Balance'.ljust(20) + str(debits) + "|" + str(credits)
    print(trialBalance)
    print("=" * 20)


if __name__ == '__main__':
    programRunning = True
    accountsList = []
    tJournal = account.Journal()
    transactionNumber = 0

    # Main Interaction Loop

    while programRunning:
        userInput = input("What ya want?\n")
        userInput = ParseInput(userInput)

        if userInput[0] == ("dr" or "cr"):
            AccountTransaction(userInput, transactionNumber)
            transactionNumber += 1
        elif userInput[0] == "addDef":
            AddDefaultAccounts()
        elif userInput[0] == ("list" or "printacc" or "printAccounts"):
            PrintAccountList()
        elif userInput[0] == ("print" or "show"):
            PrintAccount(userInput)
        elif userInput[0] == "trial":
            PrintUnajustedTrialBal()
        elif userInput[0] == "quit":
            programRunning = False

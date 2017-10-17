userString = input("Want to give me a thing?\n")

endOfString = len(userString)-1
for x in range(len(userString)):
    if userString[x] == userString[endOfString]:
        endOfString -= 1
    else:
        print("Not a palindrome.")
        quit()
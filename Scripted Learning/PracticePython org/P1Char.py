import datetime

now = datetime.datetime.now()

userYear = int(input("How old are you?\n"))
if userYear < 100:
    print("You will be 100 in %i" % (now.year + (100 - userYear)))
else:
	print("You are older than 100! Congrats...though I bet you lied.\nHowever, you turned 100 in %i." % (now.year + (100 - userYear)))
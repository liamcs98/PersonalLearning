userNumber = int(input("Yo, number?\n"))

output= ""

for x in range(1,userNumber+1):
	if userNumber % x == 0:
		output += str(x)
		output += ", "
print(output)
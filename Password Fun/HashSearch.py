import hashlib
import sys

if __name__ == '__main__':
	
	searchingForThis = input("Hey! What hashed password are you looking for? \n").strip()


	with open('rockyouInput.txt', "r", encoding="Latin-1") as f:
		lineNumber=0
		for line in f:
			line=line.strip()
			hash_object = hashlib.md5(line.encode())
			hash_object=hash_object.hexdigest()
			if hash_object == searchingForThis:
				print("\nYep! Found it! It is on line " + str(lineNumber) +". And the Password is " + line)
				quit()
			lineNumber+=1
			if lineNumber%5000 == 0:
					sys.stdout.write("\rSearching #%i" % (lineNumber))

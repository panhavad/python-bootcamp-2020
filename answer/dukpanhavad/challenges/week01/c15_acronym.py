"""
challenger: dukpanahavad
purpos: print splited word first character
"""
res = ""
#promt for user input
inputed_info = input("Enter something: ")
for word in inputed_info.split(" "):
	res = res + word[0].upper()
print(res)
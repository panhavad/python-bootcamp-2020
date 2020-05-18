"""
challenger: dukpanahavad
purpos: print index and value
"""
#promt for user input
inputed_info = input("Enter something: ")
for index, val in enumerate(inputed_info):
	print("["+ str(index) +"]"+"["+ str(val) +"]")
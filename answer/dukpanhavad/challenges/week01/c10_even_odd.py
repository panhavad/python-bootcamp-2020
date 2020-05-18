"""
challenger: dukpanahavad
purpos: even odd or bad input - string validation
"""
try:
	#promt for user input - cast float to prevent user error
	inputed_info = float(input("Enter a number: "))
	print("EVEN" if not inputed_info%2 else "ODD")
except ValueError as e:
	print("Bad input.")

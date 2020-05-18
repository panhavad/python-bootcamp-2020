"""
challenger: dukpanahavad
"""
#promt user for input
numbers = input("Enter a number: ")
try:
	print(["ODD" if int(number)%2 else "EVEN" for number in numbers.split(",")])#dont confused with the condition ahah when modulo result 0 mean false fo to else
except Exception:
	print("ERROR")
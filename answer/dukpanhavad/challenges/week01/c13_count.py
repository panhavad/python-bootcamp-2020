"""
challenger: dukpanahavad
"""
numbers = ""
#promt user for input
try:
	target_number = int(input("Enter a number: "))
	if target_number > 0:
		res_number = [each_number for each_number in range(1, target_number + 1)]
		for index, val in enumerate(res_number):
			if index == 0: #first number
				numbers = numbers + str(val)
			elif index == len(res_number):#last number
				numbers = numbers + str(val)
			else:
				numbers = numbers + "," + str(val)
		print(numbers)
	else:
		raise
except (ValueError, RuntimeError):
	print("ERROR")

"""
challenger: dukpanahavad
purpos: print file type base on extension
"""
#promt user for file name input
input_filename = input("Filename: ")
extension = input_filename.split(".")[-1].lower() #ensure case insensitive
if extension == "txt":
	print("Text File")
elif extension == "py":
	print("Python File")
elif extension == "json":
	print("JSON File")
else:
	print("Invalid Filename")

"""
challenger: dukpanahavad
purpos: get input and display -> if empty string give use instruction
"""
inputed_info = input("Enter your name: ")
print("You must enter your name. " if not len(inputed_info) else inputed_info) #TODO: done this programe with one line woohoo
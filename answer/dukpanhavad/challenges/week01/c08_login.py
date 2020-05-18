"""
challenger: dukpanahavad
purpos: validate 2 different input from user
"""

#configure username password
stored_username, stored_password = "admin", "password168"
#prompt username password from user
username, password = input("username: "), input("password: ")
#print output of validation
print("[Access Granted]" if username == stored_username and password == stored_password else "[Access Denied]") #this is case sensitive
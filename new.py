#1 Display a welcome message on the SOC wall-screen


print("Welcome to Cypher Ltd SOC")



print("Welcome to Cypher Ltd SOC")



#2 Cypher Ltd - SOC welcome banner
# Written by: John Ofulue
print("="* 34)
print("CYPHER LTD - SECURITY OPERATIONS")
print("=" * 34)
print("Analyst on duty:", "John Ofulue")
print("Shift: Monday, 08:00 - 16:00") 

print()


#3 
# Cypher Ltd asset register - my laptop
device_id = "CYP-LG-0472"
owner = "John Ofulue"
login_attempts = 2
max_logins = 3
disk_free_percent = 62.5
disk_encrypted = True
 
print("Device:", device_id, "| Owner:", owner)
print("Attempts:", login_attempts, "of", max_logins)
print("Disk free:", disk_free_percent, "% | Encrypted:", disk_encrypted)

print()

#3 data types

device_id = "CYP-LG-0472"
login_attempts = 2
disk_free_percent = 62.5
disk_encrypted = True
 
print(type(device_id))
print(type(login_attempts))
print(type(disk_free_percent))
print(type(disk_encrypted))

print()

#4 maths for analysts

login_attempts = 2
max_logins = 3
 
attempts_left = max_logins - login_attempts
percent_used = login_attempts / max_logins * 100
 
print("Attempts left:", attempts_left)
print("Percent used:", round(percent_used, 2))
print("Limit reached?", login_attempts >= max_logins)
print("Float division:", 7 / 2)
print("Whole-number division:", 7 // 2)

print()

#4 Approved Users

approved_users = ["aokafor", "tbakare", "neze", "imusa"]
print(approved_users)
print(type(approved_users))
 
# A new analyst joins: reassign the variable to the updated list
approved_users = ["aokafor", "tbakare", "neze", "imusa", "aobi"]
print(approved_users)
print("Approved users:", len(approved_users))

print()

login_attempts = 3
message = "Failed login attempts: " + str(login_attempts)
print(message)

#5 lock the account if the maximum number of login attempts has been reached

failed_attempts = 6
if failed_attempts > 5:
    print("Account locked.")


#6 else the patch check

operating_system = "Windows 10"
 
if operating_system == "Windows 11":
    print("Up to date - no action needed")
else:
    print("Update needed - raise a ticket")


import string
import random

# #all combinations of letters + puncuation + digits orginiate from here 
pass_comb = string.ascii_letters + string.punctuation  + string.digits

# #empty string 
password = "" 

#length of password - returns a number between 8-16
password_length = random.randint(8,16)

for i in range(password_length):
    #user_input = input("press any key to get password")
    #picking one character and goes through the loop each time until x number of loops are achieved. 
    final_pass = random.choice(pass_comb)
    #adding a new string character each time 
    password = password + final_pass 
    
print(password)





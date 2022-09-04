#Password generator
import random
import array
#This can be changed to suit your password length
max_len = 12
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

combined_list = digits + lowercase_characters + uppercase_characters + symbols

#Choose one of each list
rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase_characters)
rand_lower = random.choice(lowercase_characters)
rand_symbol = random.choice(symbols)

temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(combined_list)

    #prevent it from having a consistent pattern
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

#temp_password to password
password = ""
for x in temp_pass_list:
    password = password + x

#print out password    
print("This is your password: " + password)
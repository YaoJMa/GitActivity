import random
import string

pass_length = int(input ("How long do you want your password to be? "))

pass_characters = string.ascii_letters + string. digits 

password = [] 

for x in range(pass_length):
	password.append(random.choice(pass_characters))

print (''.join(password))
